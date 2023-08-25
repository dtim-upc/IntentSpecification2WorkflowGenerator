import dearpygui.dearpygui as dpg
from dearpygui_ext.themes import create_theme_imgui_light

from common import *
from demo.demo_api.functions import abstract_planner

ontology = get_ontology_graph()
datasets = {n.fragment: n for n in ontology.subjects(RDF.type, dmop.TabularDataset)}
problems = {n.fragment: n for n in ontology.subjects(RDF.type, tb.Problem)}
algorithms = {n.fragment: n for n in ontology.subjects(RDF.type, tb.Algorithm)}


def run_abstract_planner():
    intent_graph = get_graph_xp()
    intent = dpg.get_value('intent_name')
    data = dpg.get_value('dataset')
    problem = dpg.get_value('problem')

    intent_graph.add((ab.term(intent), RDF.type, tb.Intent))
    intent_graph.add((ab.term(intent), tb.overData, ab.term(data)))
    intent_graph.add((ab.term(intent), tb.tackles, cb.term(problem)))

    abstract_plans = abstract_planner(get_ontology_graph(), intent_graph)
    print('Abstract Plans created')
    dpg.set_value('abstract_plans', abstract_plans)


dpg.create_context()
dpg.create_viewport(title='Workflow Generator Demo', width=1000, height=600)
light_theme = create_theme_imgui_light()
dpg.bind_theme(light_theme)

with dpg.font_registry():
    default_font = dpg.add_font("JetBrainsMonoNerdFont-Regular.ttf", 20)

dpg.bind_font(default_font)

with dpg.window(label="Workflow Generator Demo", tag='window'):
    with dpg.collapsing_header(label="Abstract Planner", default_open=True):
        dpg.add_input_text(label="Intent Name", tag='intent_name')
        dpg.add_combo(label="Dataset", items=list(datasets.keys()), tag='dataset')
        dpg.add_combo(label="Problem", items=list(problems.keys()), tag='problem')
        dpg.add_button(label="Run Abstract Planner", callback=run_abstract_planner)

    with dpg.collapsing_header(label='Abstract Plans'):
        dpg.add_text('Generated Abstract Plans')
        with dpg.child_window(height=200, delay_search=True) as _child_id:
            for aplan in dpg.get_value('abstract_plans') or []:
                alg = next(a for a in aplan.keys() if aplan[a] == [])
                dpg.add_text(alg.fragment)



dpg.set_primary_window("window", True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
