#!/usr/bin/env python3
"""
Data Pipeline Flow Diagram
Week 1: Data Collection Lecture
Illustrates the ML data pipeline stages from collection to deployment
"""

from graphviz import Digraph
import os

OUTPUT_DIR = "../figures"
OUTPUT_FILE = "data_pipeline_flow"

def create_data_pipeline_flow():
    dot = Digraph(comment='ML Data Pipeline', format='png')
    dot.attr(rankdir='LR', dpi='300')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Arial',
            fontsize='16', height='0.6', width='1.5')
    dot.attr('edge', penwidth='2')

    # Nodes with colors
    dot.node('A', 'Collection', fillcolor='#ff9966', penwidth='4')
    dot.node('B', 'Validation', fillcolor='#99ccff')
    dot.node('C', 'Labeling', fillcolor='#99ccff')
    dot.node('D', 'Training', fillcolor='#99ccff')
    dot.node('E', 'Deployment', fillcolor='#99ccff')

    # Edges
    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'E')

    return dot

if __name__ == "__main__":
    output_dir = os.path.join(os.path.dirname(__file__), OUTPUT_DIR)
    os.makedirs(output_dir, exist_ok=True)

    dot = create_data_pipeline_flow()
    output_path = os.path.join(output_dir, OUTPUT_FILE)
    dot.render(output_path, cleanup=True)
    print(f"Generated: {output_path}.png")
