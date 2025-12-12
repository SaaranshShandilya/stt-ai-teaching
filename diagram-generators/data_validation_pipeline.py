#!/usr/bin/env python3
"""
Data Validation Pipeline Diagram
Week 2: Data Validation Lecture
Illustrates the stages of data validation from raw data to verified dataset
"""

from graphviz import Digraph
import os

OUTPUT_DIR = "../figures"
OUTPUT_FILE = "data_validation_pipeline"

def create_data_validation_pipeline():
    dot = Digraph(comment='Data Validation Pipeline', format='png')
    dot.attr(rankdir='LR', dpi='300')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Arial',
            fontsize='14', height='0.6', width='1.3')
    dot.attr('edge', penwidth='2')

    # Nodes with colors
    dot.node('A', 'Raw Data', fillcolor='#99ccff')
    dot.node('B', 'Inspection', fillcolor='#99ccff')
    dot.node('C', 'Schema\\nValidation', fillcolor='#99ccff')
    dot.node('D', 'Cleaning', fillcolor='#99ccff')
    dot.node('E', 'Drift\\nDetection', fillcolor='#99ccff')
    dot.node('F', 'Verified\\nDataset', fillcolor='#99ff99', penwidth='4')

    # Edges
    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'E')
    dot.edge('E', 'F')

    return dot

if __name__ == "__main__":
    output_dir = os.path.join(os.path.dirname(__file__), OUTPUT_DIR)
    os.makedirs(output_dir, exist_ok=True)

    dot = create_data_validation_pipeline()
    output_path = os.path.join(output_dir, OUTPUT_FILE)
    dot.render(output_path, cleanup=True)
    print(f"Generated: {output_path}.png")
