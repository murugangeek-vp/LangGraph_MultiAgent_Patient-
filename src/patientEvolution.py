from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class PatientState(TypedDict):
    patient_name: str
    physician_notes: str
    cardiologist_notes: str
    surgeon_notes: str

def general_physician_node(state: PatientState) -> dict:
    print("General physician examining", state.get('patient_name', 'Unknown'))
    notes = "Patient reports chest pain and shortness of breath. Heart rate elevated."
    return {"physician_notes": notes}

def cardiologist_node(state: PatientState) -> dict:
    print("Cardiologist examining", state.get('patient_name', 'Unknown'))
    notes = "Patient has high blood pressure and cholesterol. Needs medication."
    return {"cardiologist_notes": notes}

def surgeon_node(state: PatientState) -> dict:
    print("Surgeon examining", state.get('patient_name', 'Unknown'))
    notes = "Patient needs surgery to remove tumor."
    return {"surgeon_notes": notes}

def patient_evolution_graph():
    workflow = StateGraph(PatientState)
    workflow.add_node("general_physician", general_physician_node)
    workflow.add_node("cardiologist", cardiologist_node)
    workflow.add_node("surgeon", surgeon_node)
    
    workflow.add_edge(START, "general_physician")
    workflow.add_edge("general_physician", "cardiologist")  
    # workflow.add_conditional_edges(
    #     "general_physician",
    #     lambda state: "cardiologist" if state.get("physician_notes") else "surgeon",
    # )
    workflow.add_edge("cardiologist", "surgeon")
    workflow.add_edge("surgeon", END)
    
    return workflow.compile()

if __name__ == "__main__":
    graph = patient_evolution_graph()
    
    # Save the graph image
    try:
        png_image = graph.get_graph().draw_mermaid_png()
        with open("patient_evolution_graph.png", "wb") as f:
            f.write(png_image)
        print("Graph image saved as patient_evolution_graph.png")
    except Exception as e:
        print(f"Could not save graph image: {e}")

    state = {"patient_name": "Murugan Vadivel"}
    result = graph.invoke(state)
    print("Final State:", result)