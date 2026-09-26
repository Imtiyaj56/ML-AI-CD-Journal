%
% ================================================================
% Experiment 8: Tower of Hanoi Problem using Prolog
% ================================================================


% ----------------------------------------------------------------
% Predicate: move(N, Source, Target, Auxiliary)
% Moves N disks from Source peg to Target peg
% using Auxiliary peg.
% ----------------------------------------------------------------

% Base Case
move(1, Source, Target, _) :-
    write('Move top disk from '),
    write(Source),
    write(' to '),
    write(Target),
    nl.


% Recursive Step
move(N, Source, Target, Auxiliary) :-
    N > 1,
    M is N - 1,

    move(M, Source, Auxiliary, Target),

    move(1, Source, Target, _),

    move(M, Auxiliary, Target, Source).


% ----------------------------------------------------------------
% Helper Predicate: hanoi(N)
% ----------------------------------------------------------------

hanoi(N) :-
    write('--- Solution for '),
    write(N),
    write(' Disks ---'),
    nl,

    move(N, 'A', 'C', 'B'),

    write('-----------------------------'),
    nl.