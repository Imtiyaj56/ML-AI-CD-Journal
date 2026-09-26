%
% ================================================================
% Experiment 11: Travelling Salesperson Problem (TSP) using Prolog
% Environment: SWI-Prolog
% ================================================================


% ----------------------------------------------------------------
% 1. Facts: Symmetric road distances between cities
% ----------------------------------------------------------------

edge(a, b, 10).
edge(a, c, 15).
edge(a, d, 20).
edge(b, c, 35).
edge(b, d, 25).
edge(c, d, 30).


% Bidirectional road lookup

cost(X, Y, Dist) :-
    edge(X, Y, Dist).

cost(X, Y, Dist) :-
    edge(Y, X, Dist).


% ----------------------------------------------------------------
% 2. Tour Generation and Cost Calculation
% ----------------------------------------------------------------

% Base case

calc_path([X, Y], Total) :-
    cost(X, Y, Total).


% Recursive step

calc_path([X, Y | Rest], Total) :-

    cost(X, Y, D1),

    calc_path(
        [Y | Rest],
        D2
    ),

    Total is D1 + D2.


% Complete tour

tour(StartCity, [StartCity | Tour]) :-

    findall(
        C,
        (edge(C, _, _) ; edge(_, C, _)),
        AllCitiesWithDups
    ),

    sort(
        AllCitiesWithDups,
        AllCities
    ),

    delete(
        AllCities,
        StartCity,
        OtherCities
    ),

    permutation(
        OtherCities,
        Permutation
    ),

    append(
        Permutation,
        [StartCity],
        FullPath
    ),

    Tour = FullPath.


% ----------------------------------------------------------------
% 3. Find All Tours and Identify Optimal Route
% ----------------------------------------------------------------

all_tours(StartCity, AllTours) :-

    findall(
        Cost-Path,
        (
            tour(StartCity, Path),
            calc_path(Path, Cost)
        ),
        AllTours
    ).


% ----------------------------------------------------------------
% 4. Solver Wrapper Predicate
% ----------------------------------------------------------------

solve_tsp :-

    Start = a,

    write('----------------------------------------------------'),
    nl,

    write(' Solving TSP starting and ending at City: '),
    write(Start),
    nl,

    write('----------------------------------------------------'),
    nl,

    all_tours(
        Start,
        AllTours
    ),

    keysort(
        AllTours,
        SortedTours
    ),

    SortedTours = [MinCost-BestPath | _],

    nl,

    write('All Evaluated Valid Tours:'),
    nl,

    print_all_tours(SortedTours),

    nl,

    write('===================================================='),
    nl,

    write('OPTIMAL TOUR FOUND:'),
    nl,

    format(
        'Path : ~w~n',
        [BestPath]
    ),

    format(
        'Cost : ~w~n',
        [MinCost]
    ),

    write('===================================================='),
    nl.


print_all_tours([]).

print_all_tours([Cost-Path | Rest]) :-

    format(
        ' Route: ~w ==> Cost: ~w~n',
        [Path, Cost]
    ),

    print_all_tours(Rest).