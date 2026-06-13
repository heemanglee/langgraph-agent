# Deep Agent RAG

## Overview

Deep Agent RAG는 LangGraph 기반 Agentic RAG 시스템이다.

기존 RAG(Retrieval-Augmented Generation)는 사용자의 질문에 대해 문서를 한 번 검색한 뒤 검색 결과를 기반으로 답변을 생성한다. 이러한 방식은 구현이 단순하고 빠르지만, 최초 검색 결과가 충분하지 않은 경우 추가 탐색을 수행할 수 없다는 한계가 존재한다.

본 프로젝트는 LangGraph를 사용하여 Agent가 스스로 검색 결과를 평가하고, 필요 시 추가 검색을 수행하며, 충분한 정보를 확보할 때까지 탐색을 반복하는 Deep Agent 스타일의 RAG를 구현하는 것을 목표로 한다.

---

## Goals

본 프로젝트의 목표는 다음과 같다.

- LangGraph Agent 기반 Agentic RAG 학습
- LangGraph Agent 기반 Tool Calling 구조 구현
- Document Search Tool 기반 Agent 구현
- Agentic RAG와 Traditional RAG 비교
- Multi-Step Retrieval 구현
- Tool Calling 및 Agent Reasoning Loop 학습

---

## Problem Statement

전통적인 RAG 시스템은 일반적으로 다음과 같은 흐름으로 동작한다.

```text
User Question
    ↓
Document Retrieval
    ↓
Retrieved Documents
    ↓
LLM Answer
```

이 방식은 단순하지만 다음과 같은 한계를 가진다.

- 검색 결과가 부족해도 추가 탐색이 불가능하다.
- 최초 검색어 품질에 크게 의존한다.
- 관련 정보가 여러 문서에 분산되어 있는 경우 검색 품질이 저하될 수 있다.
- 검색 실패 시 답변 품질이 급격히 저하된다.
- 검색 결과의 충분성을 판단할 수 없다.

---

## Deep Agent Approach

```text
User Question
    ↓
LangGraph Agent
    ↓
Thought
    ↓
Document Search Tool
    ↓
Observation
    ↓
Thought
    ↓
Document Search Tool
    ↓
Observation
    ↓
Answer
```

Agent는 다음과 같은 과정을 반복 수행한다.

1. 질문 분석  
2. Tool 호출 여부 판단  
3. 문서 검색  
4. 검색 결과 분석  
5. 추가 Tool 호출 여부 판단  
6. Tool 호출 전략 결정  
7. Reasoning Loop 반복  
8. 최종 답변 생성

---

## Architecture

```text
User
 ↓
LangGraph Agent
 ↓
Thought
 ↓
Tool Call
 ↓
Observation
 ↓
Thought
 ↓
Tool Call
 ↓
Observation
 ↓
Answer
```

The Agent decides autonomously whether another tool call is required. Developers do not define conditional edges, search loops, or re-planning workflows. The Agent repeatedly performs reasoning and tool usage until it determines that a final answer can be generated.

---

## Core Components

### LangGraph Agent

LangGraph Agent는 시스템의 핵심 의사결정 주체이다.

Agent는 Tool 목록과 시스템 프롬프트만 제공받으며, 어떤 Tool을 호출할지, 추가 Tool 호출이 필요한지, 언제 답변할지를 스스로 판단한다.

주요 역할

- 사용자 질문 분석
- Tool 호출 여부 판단
- 검색 결과 해석
- 추가 Tool 호출 여부 판단
- 답변 생성

본 프로젝트는 Node 기반 Workflow보다 ReAct Agent 패턴을 우선적으로 사용한다.

---

### Document Search Tool

Document Search Tool은 Agent가 사용할 수 있는 유일한 Tool이다.

Agent는 문서 검색이 필요하다고 판단할 경우 해당 Tool을 호출한다.

예시:

```text
Search Documents:
"Celery worker memory optimization"
```

Tool 내부 구현은 Agent와 분리된다.

예시:

- Vector Search
- Metadata Filtering
- Hybrid Search
- Reranking

Agent는 검색 결과만 전달받는다.

---

### Retrieval Layer

Retrieval Layer는 실제 문서 검색을 수행한다.

초기 버전에서는 OpenSearch 기반 Retrieval을 사용한다.

향후 다음 기능을 추가할 수 있다.

- Hybrid Search
- Query Expansion
- Multi Query Retrieval
- Reranking
- Retrieval Evaluation

---

## ReAct Loop

```text
Thought
 ↓
Action (Tool Call)
 ↓
Observation
 ↓
Thought
 ↓
Action (Tool Call)
 ↓
Observation
 ↓
Answer
```

The project uses the ReAct (Reasoning + Acting) pattern. Rather than predefined Planner, Search, and Answer nodes, the LangGraph Agent iteratively reasons, invokes tools, observes results, and continues until it has enough information to answer.

---

## MVP Scope

초기 버전에서는 다음 기능만 구현한다.

### Included

- LangGraph Agent
- Document Search Tool
- OpenSearch Retrieval
- ReAct Agent Loop
- Final Answer Generation

### Excluded

- Web Search
- Code Execution
- Multi-Agent Collaboration
- Long-Term Memory
- Human Feedback Loop
- External Knowledge Sources
- Answer Verification Agent

---

## Success Criteria

프로젝트 성공 기준은 다음과 같다.

- Agent가 최소 1회 이상 문서 검색을 수행한다.  
- Agent가 Tool 결과를 기반으로 추론할 수 있다.  
- Agent가 필요 시 추가 검색을 수행할 수 있다.  
- Agent가 검색 결과를 기반으로 답변을 생성할 수 있다.  
- Agent의 Reasoning 및 Tool Calling 과정을 추적할 수 있다.  
- Traditional RAG 대비 Agentic RAG의 동작 차이를 확인할 수 있다.

---

## Future Roadmap

### Phase 1

- Basic Deep Agent RAG
- LangGraph Agent
- Document Search Tool
- OpenSearch Retrieval
- Multi-Step Retrieval

### Phase 2

- Query Rewriting
- Query Expansion
- Retrieval Evaluation

### Phase 3

- Hybrid Search
- Multi Query Retrieval
- Reranking

### Phase 4

- Answer Verification Agent
- Citation Generation
- Confidence Scoring

### Phase 5

- Multi-Agent Architecture
- Specialized Research Agents
- Autonomous Knowledge Exploration

---

## Learning Objectives

본 프로젝트는 단순히 RAG 시스템을 구현하는 것이 목적이 아니다.

다음과 같은 Agent Engineering 역량을 학습하는 것을 목표로 한다.

- LangGraph Agent 구조 이해
- ReAct Agent 패턴 학습
- Tool Calling 구조
- ReAct Reasoning Loop 이해
- Multi-Step Reasoning
- Agentic Retrieval
- LangGraph 활용
- Deep Agent 아키텍처 이해
