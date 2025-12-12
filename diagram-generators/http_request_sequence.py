"""
HTTP Request Sequence Diagram
Week 1: Data Collection Lecture
Illustrates the client-server interaction for an HTTP API request
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

def create_http_request_sequence():
    """Simple sequence diagram using basic matplotlib shapes"""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    client_x, server_x = 2, 8

    # Participant boxes
    for x, label in [(client_x, "Client\n(Browser/Python)"), (server_x, "Server\n(OMDb)")]:
        box = FancyBboxPatch((x - 0.7, 6.8), 1.4, 0.8, boxstyle="round,pad=0.1",
                            facecolor='#e8f4f8', edgecolor='#333', linewidth=2)
        ax.add_patch(box)
        ax.text(x, 7.2, label, ha='center', va='center', fontsize=11, weight='bold')

    # Lifelines
    for x in [client_x, server_x]:
        ax.plot([x, x], [0.5, 6.8], 'k--', linewidth=1, alpha=0.5)

    # Message 1: Request
    y1 = 5.5
    ax.annotate('', xy=(server_x, y1), xytext=(client_x, y1),
                arrowprops=dict(arrowstyle='->', lw=2, color='#2563eb'))
    ax.text(5, y1 + 0.3, 'HTTP Request\nGET /movie?t=Inception',
            ha='center', fontsize=10, weight='bold',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor='none'))
    ax.text(client_x - 1.3, y1 - 0.4, 'Headers: User-Agent, Auth',
            ha='right', fontsize=8, style='italic', color='#64748b')

    # Message 2: Processing (self-call)
    y2 = 3.5
    box = FancyBboxPatch((server_x, y2 - 0.25), 0.8, 0.5,
                        facecolor='#fff9e6', edgecolor='#666', linewidth=1.5)
    ax.add_patch(box)
    ax.text(server_x + 0.4, y2, 'Process Request\n(Query DB)',
            ha='center', va='center', fontsize=9, style='italic')

    # Message 3: Response
    y3 = 1.5
    ax.annotate('', xy=(client_x, y3), xytext=(server_x, y3),
                arrowprops=dict(arrowstyle='->', lw=2, color='#059669', linestyle='dashed'))
    ax.text(5, y3 + 0.3, 'HTTP Response\n(JSON Data)',
            ha='center', fontsize=10, weight='bold',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor='none'))
    ax.text(server_x + 1.3, y3 - 0.4, 'Status: 200 OK',
            ha='left', fontsize=8, style='italic', color='#64748b')

    plt.tight_layout()
    return fig

OUTPUT_DIR = "../figures"
OUTPUT_FILE = "http_request_sequence.png"

if __name__ == "__main__":
    output_dir = os.path.join(os.path.dirname(__file__), OUTPUT_DIR)
    os.makedirs(output_dir, exist_ok=True)

    fig = create_http_request_sequence()
    output_path = os.path.join(output_dir, OUTPUT_FILE)
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Generated: {output_path}")
    plt.close()
