# Architecture Documentation

## Overview

The Multi-Agent Orchestration Framework implements a hierarchical agent architecture that routes customer queries to specialized agents based on intent. This document provides detailed insights into the system architecture, design patterns, and implementation details.

## System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        User Interface                        │
│                  (CLI, API, or Application)                  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   Orchestrator Agent                         │
│              (Intent Recognition & Routing)                  │
└───────────┬─────────────────────────────┬───────────────────┘
            │                             │
            ▼                             ▼
┌─────────────────────────┐   ┌─────────────────────────────┐
│  Parts Support Agent    │   │    Parts Sales Agent        │
│                         │   │                             │
│  - Order Status         │   │  - Part Details             │
│  - Refund Status        │   │  - Compatibility            │
│  - Subscription Mgmt    │   │  - Shipping Info            │
└──────────┬──────────────┘   └──────────┬──────────────────┘
           │                              │
           ▼                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      Function Tools                          │
│  ┌────────────┐  ┌────────────┐  ┌──────────────────┐      │
│  │ Order      │  │Subscription│  │ Parts Lookup     │      │
│  │ Tools      │  │ Tools      │  │ Tool             │      │
│  └────────────┘  └────────────┘  └──────────────────┘      │
└──────────┬──────────────────────────────┬───────────────────┘
           │                              │
           ▼                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      API Client Layer                        │
└──────────┬──────────────────────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────────────────────┐
│                    External REST APIs                        │
└─────────────────────────────────────────────────────────────┘
```

## Core Components

### 1. Orchestrator Agent

**Purpose**: Routes incoming queries to the appropriate specialized agent based on intent analysis.

**Key Responsibilities**:
- Analyze user queries to understand intent
- Select the appropriate specialized agent
- Delegate query execution to the selected agent
- Return formatted responses to the user

**Implementation Details**:
- Uses OpenAI's function calling for intent detection
- Defines two primary routing functions: `parts_support_tool` and `parts_sales_tool`
- Maintains single responsibility: routing only

### 2. Specialized Agents

#### Parts Support Agent

**Purpose**: Handle customer support queries related to orders, refunds, and subscriptions.

**Available Tools**:
- `parts_get_order_status_tool`: Query order status and tracking
- `parts_get_refund_status_tool`: Check refund status
- `parts_subscription_lookup_tool`: Lookup subscription details
- `parts_subscription_cancel_tool`: Cancel subscriptions
- `parts_subscription_update_tool`: Update subscription settings

**Design Pattern**: Specialist pattern - focused on a specific domain

#### Parts Sales Agent

**Purpose**: Handle sales and product information queries.

**Available Tools**:
- `get_part_details_tool`: Retrieve part specifications, compatibility, and shipping info

**Design Pattern**: Specialist pattern - focused on product information

### 3. Function Tools

Function tools are decorated Python functions that serve as the bridge between agents and external APIs.

**Design Principles**:
- Single Responsibility: Each tool handles one specific operation
- Clear Interfaces: Well-defined inputs and outputs
- Error Handling: Graceful error handling and reporting
- Type Safety: Full type hints for better IDE support

**Tool Categories**:

1. **Order Tools** (`src/tools/order_tools.py`)
   - Order status lookup
   - Refund status checking

2. **Subscription Tools** (`src/tools/subscription_tools.py`)
   - Subscription lookup
   - Subscription cancellation
   - Subscription updates

3. **Parts Tools** (`src/tools/parts_tools.py`)
   - Part details and specifications
   - Model compatibility checking
   - Shipping information

### 4. API Client Layer

**Purpose**: Provide a consistent interface for HTTP requests to external APIs.

**Components**:

1. **APIClient** (`src/api/client.py`)
   - Handles HTTP POST requests
   - Implements error handling and retries
   - Provides consistent error responses

2. **APIConfig** (`src/api/config.py`)
   - Manages API endpoints and configuration
   - Loads environment variables
   - Provides configuration objects

## Design Patterns

### 1. Hierarchical Agent Pattern

The system uses a hierarchical structure where:
- **Level 1**: Orchestrator (decision maker)
- **Level 2**: Specialized agents (domain experts)
- **Level 3**: Function tools (execution layer)

This pattern provides:
- Clear separation of concerns
- Easy extensibility (add new agents or tools)
- Maintainable codebase

### 2. Function Tool Pattern

Function tools are decorated with `@function_tool` to enable:
- Automatic schema generation
- Integration with agent framework
- Type-safe function calling

### 3. Configuration Pattern

Configuration is centralized and uses:
- Environment variables for sensitive data
- Default values for optional settings
- Validation at initialization

## Data Flow

### Example: Order Status Query

```
1. User Query: "Check order W174191"
   ↓
2. Orchestrator Agent analyzes intent
   ↓
3. Routes to Parts Support Agent via parts_support_tool
   ↓
4. Support Agent calls parts_get_order_status_tool
   ↓
5. Tool calls APIClient.post("/parts/status", {...})
   ↓
6. API returns order details
   ↓
7. Tool returns formatted response
   ↓
8. Agent processes and formats for user
   ↓
9. Orchestrator returns final response to user
```

## Extension Points

### Adding New Agents

1. Create agent definition in `src/agents/`
2. Define agent tools and instructions
3. Create function tool wrapper in orchestrator
4. Update orchestrator instructions to include new routing logic

### Adding New Tools

1. Create tool function in appropriate `src/tools/` module
2. Decorate with `@function_tool`
3. Add tool to relevant agent's tool list
4. Update agent instructions if needed

### Adding New APIs

1. Update `src/api/config.py` with new endpoints
2. Create tool functions in `src/tools/`
3. Integrate with existing or new agents

## Error Handling Strategy

### Levels of Error Handling

1. **API Client Level**: HTTP errors, timeouts, connection errors
2. **Tool Level**: Invalid parameters, API errors
3. **Agent Level**: Tool execution errors, invalid queries
4. **Orchestrator Level**: Agent routing errors

### Error Response Format

All errors are returned in a consistent format:
```json
{
    "error": "Error type",
    "details": "Detailed error message"
}
```

## Security Considerations

1. **API Keys**: Stored in environment variables, never in code
2. **Input Validation**: All tool inputs are type-checked
3. **Error Messages**: Sensitive information is not exposed in errors
4. **Configuration**: Sensitive config is in `.env` (gitignored)

## Performance Considerations

1. **Async Operations**: All agent operations use async/await
2. **Connection Pooling**: API client reuses connections
3. **Timeout Management**: Configurable request timeouts
4. **Retry Logic**: Configurable retry attempts for failed requests

## Testing Strategy

1. **Unit Tests**: Test individual tools and components
2. **Integration Tests**: Test agent-tool interactions
3. **End-to-End Tests**: Test complete query flows
4. **Mock APIs**: Use mock responses for testing

## Future Enhancements

Potential areas for expansion:

1. **Agent Memory**: Add conversation history and context
2. **Tool Chaining**: Enable tools to call other tools
3. **Parallel Execution**: Execute multiple tools simultaneously
4. **Streaming Responses**: Support streaming for long-running operations
5. **Agent Learning**: Implement feedback loops for improved routing
6. **Additional Agents**: Add more specialized agents for different domains
7. **Multi-turn Conversations**: Support complex, multi-step interactions
8. **Tool Result Caching**: Cache frequent tool results for performance

## Conclusion

This architecture provides a solid foundation for building scalable, maintainable multi-agent systems. The clear separation of concerns, extensible design, and comprehensive error handling make it suitable for production use and further development.
