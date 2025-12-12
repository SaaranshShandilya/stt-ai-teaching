"""
Sync vs Async Request Timing Diagram
Week 1: Data Collection Lecture
Illustrates the time difference between synchronous and asynchronous request handling
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os

def create_sync_vs_async_timing():
    """Simple timing comparison using bar charts"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 5), sharex=True)

    # Synchronous requests
    sync_data = [
        ("Request 1", 0, 2, '#3b82f6'),
        ("Request 2", 2, 4, '#8b5cf6'),
        ("Request 3", 4, 6, '#ec4899'),
    ]

    ax1.set_xlim(0, 7)
    ax1.set_ylim(0, 1)
    ax1.set_title('Synchronous (Sequential)', fontsize=13, weight='bold', pad=10)
    ax1.set_yticks([])

    for label, start, end, color in sync_data:
        width = end - start
        rect = Rectangle((start, 0.2), width, 0.6, facecolor=color, edgecolor='#1e293b', linewidth=2)
        ax1.add_patch(rect)
        ax1.text(start + width/2, 0.5, label, ha='center', va='center',
                fontsize=11, weight='bold', color='white')

    # Total time arrow
    ax1.annotate('', xy=(6, 0.95), xytext=(0, 0.95),
                arrowprops=dict(arrowstyle='<->', color='#ef4444', lw=2))
    ax1.text(3, 0.95, 'Total: 6 sec', ha='center', va='bottom',
            fontsize=10, weight='bold', color='#ef4444')

    # Asynchronous requests
    async_data = [
        ("Request 1", 0.0, 2.0, '#3b82f6', 0.2),
        ("Request 2", 0.1, 2.1, '#8b5cf6', 0.5),
        ("Request 3", 0.2, 2.2, '#ec4899', 0.8),
    ]

    ax2.set_xlim(0, 7)
    ax2.set_ylim(0, 1.5)
    ax2.set_title('Asynchronous (Concurrent)', fontsize=13, weight='bold', pad=10)
    ax2.set_yticks([])
    ax2.set_xlabel('Time (seconds)', fontsize=11)

    for label, start, end, color, y_offset in async_data:
        width = end - start
        rect = Rectangle((start, y_offset), width, 0.25, facecolor=color, edgecolor='#1e293b', linewidth=2)
        ax2.add_patch(rect)
        ax2.text(start + width/2, y_offset + 0.125, label, ha='center', va='center',
                fontsize=11, weight='bold', color='white')

    # Total time arrow
    ax2.annotate('', xy=(2.2, 1.35), xytext=(0, 1.35),
                arrowprops=dict(arrowstyle='<->', color='#22c55e', lw=2))
    ax2.text(1.1, 1.35, 'Total: 2.2 sec', ha='center', va='bottom',
            fontsize=10, weight='bold', color='#22c55e')

    # Grid
    for ax in [ax1, ax2]:
        ax.grid(axis='x', alpha=0.3, linestyle='--')
        ax.set_xticks(range(0, 8))

    plt.tight_layout()
    return fig

OUTPUT_DIR = "../figures"
OUTPUT_FILE = "sync_vs_async_timing.png"

if __name__ == "__main__":
    output_dir = os.path.join(os.path.dirname(__file__), OUTPUT_DIR)
    os.makedirs(output_dir, exist_ok=True)

    fig = create_sync_vs_async_timing()
    output_path = os.path.join(output_dir, OUTPUT_FILE)
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Generated: {output_path}")
    plt.close()
