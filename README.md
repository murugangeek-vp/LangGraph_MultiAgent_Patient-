# LangGraph Multi-Agent Patient Evolution

This project demonstrates a simple multi-agent workflow using **LangGraph**. It models a patient evaluation process where a patient is sequentially examined by different specialists: a general physician, a cardiologist, and a surgeon. The state of the patient, including notes from each specialist, is passed along the graph nodes to simulate an evolving medical diagnosis workflow.

## Features

- **Sequential Medical Workflow**: Demonstrates a sequential node execution in LangGraph, moving from General Physician -> Cardiologist -> Surgeon.
- **Typed State Management**: Utilizes `TypedDict` to securely manage the patient's evolving state (e.g., patient name, physician notes, cardiologist notes, and surgeon notes) across different nodes.
- **Automated Graph Visualization**: Automatically renders and saves a diagram of the LangGraph schema (`patient_evolution_graph.png`) using `draw_mermaid_png()`.

## Prerequisites

- Python 3.8+
- [LangGraph](https://python.langchain.com/docs/langgraph) library

## Overview of the Workflow

1. **START** -> **General Physician Node**: The general physician examines the patient and adds notes regarding the initial diagnosis (e.g., chest pain, shortness of breath).
2. **General Physician Node** -> **Cardiologist Node**: The cardiologist receives the patient's state, performs an examination, and records notes (e.g., blood pressure, medication needs).
3. **Cardiologist Node** -> **Surgeon Node**: Finally, the surgeon examines the patient and records notes for further procedure (e.g., surgery).
4. **Surgeon Node** -> **END**: The workflow concludes, yielding the final consolidated patient state.

## Project Structure

```text
LangGraph_MultiAgent_Patient/
├── src/
│   └── patientEvolution.py     # Main application file containing the LangGraph logic
├── patient_evolution_graph.png # Auto-generated diagram of the workflow
└── README.md                   # Project documentation
```

## How to Run

1. Navigate to the project directory:
   ```bash
   cd f:\AI\LangGraph_MultiAgent_Patient
   ```

2. (Optional) Install the necessary dependencies if you haven't already:
   ```bash
   pip install langgraph
   ```

3. Run the script:
   ```bash
   python src/patientEvolution.py
   ```

4. **Expected Output**:
   The script will print the execution steps in the terminal and finally output the complete `PatientState` dictionary:
   ```text
   Graph image saved as patient_evolution_graph.png
   General physician examining [...]
   Cardiologist examining [...]
   Surgeon examining [...]
   Final State: {'patient_name': '...', 'physician_notes': '...', 'cardiologist_notes': '...', 'surgeon_notes': '...'}
   ```

## Customization

You can dynamically change the patient being examined by modifying the state passed into the `graph.invoke()` method inside `patientEvolution.py`:

```python
state = {"patient_name": "Your Patient Name"}
result = graph.invoke(state)
```

Additionally, edges can be changed back to `conditional_edges` to route patients only to the specific specialists they require based on their condition.
