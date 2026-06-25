import gradio as gr
from generate import ask

def handle_query(question):
    if not question.strip():
        return "Please enter a question.", ""
    
    result = ask(question)
    sources = "\n".join(f"• {s}" for s in result["sources"])
    return result["answer"], sources

with gr.Blocks(title="SCU Unofficial Guide") as demo:
    gr.Markdown("# SCU Unofficial Guide")
    gr.Markdown("Ask anything about SCU CS and Business professors based on real student reviews.")
    
    inp = gr.Textbox(
        label="Your question",
        placeholder="e.g. Is Natalie Linnell a tough grader?",
        lines=2
    )
    btn = gr.Button("Ask", variant="primary")
    answer = gr.Textbox(label="Answer", lines=8)
    sources = gr.Textbox(label="Retrieved from", lines=4)
    
    btn.click(handle_query, inputs=inp, outputs=[answer, sources])
    inp.submit(handle_query, inputs=inp, outputs=[answer, sources])

demo.launch()