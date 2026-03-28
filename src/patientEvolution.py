from langgraph.graph import StateGraph,START,END
from typing import TypedDict
class PatientState(TypedDict):
    paitentName: str
    pysician_note: str
    cardiologist_note: str
    surgeon_note: str

def general_physician_node(state: PatientState)-> dict:
    print("General physician examing",state['patient_name'])
    notes = "Patient reports chest pain and shortness of breath. Heart rate elevated."
    return {"physician notes":notes}

def cardiologist_node(state: PatientState)-> dict:
    print("Cardiologist examing",state['patient_name'])
    notes = "Patient has high blood pressure and cholesterol. Needs medication."
    return {"cardiologist notes":notes}

def surgeon_node(state: PatientState)-> dict:
    print("Surgeon examing",state['patient_name'])
    notes = "Patient needs surgery to remove tumor."
    return {"surgeon notes":notes}

def patient_evolution_graph():
    workflow = StateGraph(PatientState)
    workflow.add_node("general_physician",general_physician_node)
    workflow.add_node("cardiologist",cardiologist_node)
    workflow.add_node("surgeon",surgeon_node)
    workflow.add_edge(START,"general_physician")
    workflow.add_conditional_edges(
        "general_physician",
        lambda state: "cardiologist" if state["physician_notes"] else "surgeon",
    )
    workflow.add_edge("cardiologist","surgeon")
    workflow.add_edge("surgeon",END)
    return workflow.compile()

if __name__ == "__main__":
    graph = patient_evolution_graph()
    state = {"patient_name":"John Doe"}
    result = graph.invoke(state)
    print(result)