"""
Day 10 Part 2: Joltage Counter Configuration

Solves using Mixed Integer Linear Programming (MILP) for optimal solutions.

Mathematical formulation:
    minimize:    sum(x)
    subject to:  A·x = target
                 x ≥ 0
                 x ∈ ℤ (integers)

Where x[i] = number of presses for button i.

This guarantees we find the MINIMUM number of button presses.
"""

import time
from tqdm import tqdm

from src import solve_machine
from src.utils import parse_machine, verify_solution


def main():
    """Solve all machines and report total button presses."""
    start_time = time.time()
    
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    total_presses = 0
    stats = {}
    failed_machines = []
    
    # Process with tqdm - clean progress bar without clutter
    pbar = tqdm(lines, desc="Processing machines", unit=" machine", 
                dynamic_ncols=True, leave=True, position=0)
    
    for idx, line in enumerate(pbar):
        targets, buttons = parse_machine(line)
        n_counters = len(targets)
        n_buttons = len(buttons)
        
        min_presses, solution, method = solve_machine(targets, buttons)
        
        # Verify solution
        if min_presses != -1:
            if not verify_solution(solution, buttons, targets):
                min_presses = -1
                method = "verification-failed"
        
        if min_presses == -1:
            stats["failed"] = stats.get("failed", 0) + 1
            failed_machines.append({
                "idx": idx + 1,
                "line": line,
                "n_buttons": n_buttons,
                "n_counters": n_counters,
                "ratio": n_buttons / n_counters if n_counters > 0 else 1,
                "targets": targets,
                "method": method
            })
        else:
            stats[method] = stats.get(method, 0) + 1
            total_presses += min_presses
    
    pbar.close()
    elapsed_time = time.time() - start_time
    
    # Always write failed machines file (even if empty)
    with open('failed_machines_final.txt', 'w') as f:
        f.write(f"Failed Machines - {len(failed_machines)} total\n")
        f.write("="*70 + "\n\n")
        if failed_machines:
            for m in failed_machines:
                f.write(f"Machine #{m['idx']} - Method: {m['method']}\n")
                f.write(f"  Buttons: {m['n_buttons']}, Counters: {m['n_counters']}, ")
                f.write(f"Ratio: {m['ratio']:.2f}\n")
                f.write(f"  Targets: {m['targets']}\n")
                f.write(f"  Input: {m['line']}\n")
                f.write("-"*70 + "\n\n")
        else:
            f.write("All machines solved successfully! 🎉\n")
    
    # Print header after progress bar completes
    print(f"\n{'='*70}")
    print(f"  Day 10 Part 2: Joltage Counter Configuration")
    print(f"  Solved {len(lines)} machines")
    print(f"{'='*70}")
    print(f"Total button presses: {total_presses}")
    print(f"Machines solved: {sum(stats.values()) - stats.get('failed', 0)}/{len(lines)}")
    print(f"Elapsed time: {elapsed_time:.2f}s ({elapsed_time/len(lines)*1000:.1f}ms per machine)")
    
    print(f"\nSolution methods:")
    for method, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
        print(f"  {method:30s}: {count:3d} machines")
    
    if failed_machines:
        print(f"\n⚠️  {len(failed_machines)} machines failed")
        print(f"    Details saved to: failed_machines_final.txt")
        print(f"\nFailed machines:")
        for m in failed_machines:
            print(f"  M{m['idx']:3d}: B:{m['n_buttons']:2d} C:{m['n_counters']:2d} "
                  f"Ratio:{m['ratio']:.2f} [{m['method']}]")
    else:
        print(f"\n✅ All machines solved successfully!")
    
    print(f"{'='*70}\n")
    
    return total_presses


if __name__ == "__main__":
    result = main()
    print(f"Answer: {result}")
