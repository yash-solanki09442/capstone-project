# ADR 0001: Use Node.js Microservice for Real-Time Notifications

Date: 2026-03-02  
Status: Accepted  

## Context

The system requires real-time notification capabilities for events such as:

- Task status updates
- Comment creation
- Future user mentions

The core backend is implemented using Django and Django REST Framework.
The application follows a monolithic architecture for domain modeling, authentication, 
authorization, and CRUD operations.

However, real-time communication requires:

- Long-lived WebSocket connections
- High concurrency handling
- Efficient non-blocking I/O
- Event-driven broadcasting

We evaluated whether to implement WebSocket support directly within Django 
(using Django Channels) or to introduce a separate specialized service.

## Decision

We will implement real-time communication using a separate Node.js microservice.

The Django application remains the single source of truth for:

- Business logic
- Database persistence
- Domain validation
- Authentication

After state changes (e.g., task updates), Django will emit an internal HTTP request 
to the Node.js service, which will broadcast events to connected WebSocket clients.

This establishes a hybrid architecture:

- Monolithic core (Django)
- Specialized real-time microservice (Node.js)

## Rationale

Django Strengths:
- Batteries-included framework
- Mature ORM and authentication system
- Strong transactional guarantees
- Ideal for CRUD-heavy domain logic

Node.js Strengths:
- Event-driven architecture
- Single-threaded event loop
- Non-blocking I/O
- Efficient handling of concurrent WebSocket connections

By separating concerns:

- Domain logic remains centralized and consistent.
- Real-time concerns are isolated and optimized.
- Each component uses the most appropriate technology.

## Consequences

Positive:
- Improved scalability for real-time features
- Clear separation of responsibilities
- Technology chosen based on workload type
- Aligns with production-grade architectural patterns

Negative:
- Increased operational complexity (two services)
- Requires inter-service communication
- Deployment and monitoring become more involved

## Alternatives Considered

1. Implement WebSockets in Django using Django Channels
   - Pros: Single service, simpler deployment
   - Cons: Increased async complexity, mixed responsibilities

2. Use a message broker (e.g., Redis Pub/Sub) with Django only
   - Pros: Reduced service count
   - Cons: Still couples real-time logic to monolith

3. Full microservices architecture
   - Rejected as over-engineering for current scope

## Status

Accepted and implemented as part of Week 4 of the accelerator roadmap.