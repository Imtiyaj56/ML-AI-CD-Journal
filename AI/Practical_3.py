def dfs_water_jug(cap_a, cap_b, target):
    """
    Solves the Water Jug problem using Depth-First Search (DFS).
    cap_a: Capacity of Jug A
    cap_b: Capacity of Jug B
    target: Desired amount of water in either Jug A or Jug B
    """

    if target > max(cap_a, cap_b):
        print("Target cannot be larger than the capacities of the jugs.")
        return

    # Initial state: both jugs are empty
    initial_state = (0, 0)

    # Stack stores tuples: ((current_a, current_b), [path_of_steps])
    stack = [(initial_state, [initial_state])]

    # Set to record visited states
    visited = set()

    print(
        f"Searching for a solution using DFS to get {target}L "
        f"using jugs of {cap_a}L and {cap_b}L...\n"
    )

    while stack:
        # LIFO operation
        (curr_a, curr_b), path = stack.pop()

        # Skip if already processed
        if (curr_a, curr_b) in visited:
            continue

        visited.add((curr_a, curr_b))

        # Goal Test
        if curr_a == target or curr_b == target:
            print("Goal state reached successfully via DFS!")
            print(f"Total steps required: {len(path) - 1}\n")
            print("Step-by-step state transitions (Jug A, Jug B):")

            for step_no, state in enumerate(path):
                print(
                    f"Step {step_no}: Jug A = {state[0]}L, "
                    f"Jug B = {state[1]}L"
                )
            return

        # Generate all 6 legal successor states
        next_states = [
            (cap_a, curr_b),  # 1. Fill Jug A
            (curr_a, cap_b),  # 2. Fill Jug B
            (0, curr_b),      # 3. Empty Jug A
            (curr_a, 0),      # 4. Empty Jug B

            # 5. Pour Jug A -> Jug B
            (
                curr_a - min(curr_a, cap_b - curr_b),
                curr_b + min(curr_a, cap_b - curr_b)
            ),

            # 6. Pour Jug B -> Jug A
            (
                curr_a + min(curr_b, cap_a - curr_a),
                curr_b - min(curr_b, cap_a - curr_a)
            )
        ]

        # Push valid unvisited successors onto the stack
        for state in next_states:
            if state not in visited:
                stack.append((state, path + [state]))

    print("No solution exists for the given inputs.")


if __name__ == "__main__":
    jug_a_capacity = 4
    jug_b_capacity = 3
    target_amount = 2

    dfs_water_jug(jug_a_capacity, jug_b_capacity, target_amount)