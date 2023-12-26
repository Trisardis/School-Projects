/* Facts */
age(23,henry).
age(56,richard).
age(81,robert).
age(83,joel).
age(102,victor).
age(105,jim).
age(103,roland).
age(102,nathaniel).
age(54,franklin).
age(55,ryan).
age(17,louis).
age(84,rickie).
age(53,peter).
age(105,herman).
age(100,rolando).
age(80,alexander).
age(53,sean).
age(25,sam).
age(19,will).
age(105,sonny).
age(80,willie).
age(50,rory).
age(140,raleigh).
age(54,sherrie).
age(84,josie).
age(83,tina).
age(108,judy).
age(104,martha).
age(106,kristin).
age(105,sally).
age(56,meghan).
age(29,chelsea).
age(20,erika).
age(52,emily).
age(50,susana).
age(21,aurora).
age(18,anna).
age(108,wanda).
age(106,marta).
age(84,brittney).
age(56,sarah).
age(107,diane).
age(78,jane).
age(48,traci).
age(20,wendy).
age(137,ollie).

parent(richard,henry).
parent(sherrie,henry).
parent(richard,erika).
parent(sherrie,erika).
parent(joel,richard).
parent(tina,richard).
parent(joel,meghan).
parent(tina,meghan).
parent(robert,sherrie).
parent(josie,sherrie).
parent(robert,ryan).
parent(josie,ryan).
parent(jim,robert).
parent(martha,robert).
parent(victor,josie).
parent(judy,josie).
parent(victor,rachel).
parent(judy,rachel).
parent(nathaniel,joel).
parent(sally,joel).
parent(roland,tina).
parent(kristin,tina).
parent(meghan,chelsea).
parent(franklin,chelsea).
parent(ryan,louis).
parent(emily,louis).
parent(ryan,sam).
parent(emily,sam).
parent(rachel,peter).
parent(rickie,peter).
parent(peter,aurora).
parent(susana,aurora).
parent(peter,anna).
parent(susana,anna).
parent(sean,will).
parent(sarah,will).
parent(alexander,emily).
parent(brittney,emily).
parent(alexander,sean).
parent(brittney,sean).
parent(herman,alexander).
parent(wanda,alexander).
parent(marta,brittney).
parent(rolando,brittney).
parent(sonny,willie).
parent(diane,willie).
parent(willie,rory).
parent(jane,rory).
parent(rory,wendy).
parent(traci,wendy).
parent(raleigh,victor).
parent(ollie,victor).
parent(raleigh,sonny).
parent(ollie,sonny).

/* Rules */
sibling(X,Y) :- parent(Z, X), parent(Z, Y), X\=Y.

grandparent(X,Y):-parent(X,P) , parent(P,Y).

% Define a predicate to find the Nth ancestor relationship
nth_ancestor(Parent, Child, 1) :- parent(Parent, Child).
nth_ancestor(Parent, Child, N) :- 
    NN is N-1, NN > 0, 
    parent(InBetween, Child),
    nth_ancestor(Parent, InBetween, NN).

% Define a predicate to find the Nth cousin K times removed
nthcousinkremoved(X, Y, N, K) :-
    nth_cousin(X, Z, N),
    kth_descendant(Z, Y, K),
	K >= 0,
	N >= 0.

% Rule: Find the k-th descendant
kth_descendant(Ancestor, Descendant, K) :-
    K >= 0,
    descendant(Ancestor, Descendant, K).

% Base case: Ancestor is the direct ancestor of Descendant
descendant(Ancestor, Descendant, 0) :-
    Ancestor = Descendant.

% Base case: Ancestor is the direct parent of Descendant
descendant(Ancestor, Descendant, 1) :-
    parent(Ancestor, Descendant).

% Recursive case: Ancestor is the ancestor of Descendant
descendant(Ancestor, Descendant, K) :-
    K > 1,
    parent(Ancestor, Intermediate),
    K1 is K - 1,
    descendant(Intermediate, Descendant, K1).

% Define a predicate to find the Nth cousin relationship
nth_cousin(Child1, Child2, N) :-
    nth_ancestor(Parent1, Child1, N),
    nth_ancestor(Parent2, Child2, N),
    sibling(Parent1, Parent2).


% kth child of a parent
% Define a predicate to find the kth child of a parent after sorting by age
kthchild(KthChild, Parent, K) :-
    kth_child(Parent, SortedChildren),
    nth1(K, SortedChildren, KthChild).

% Sort children by age for each parent
kth_child(Parent, SortedChildren) :-
    findall(Child, parent(Parent, Child), Children),
    predsort(compare_ages, Children, SortedChildren).

% Define a predicate to compare ages for sorting
compare_ages(Order, Child1, Child2) :-
    age(Age1, Child1),
    age(Age2, Child2),
    compare(Order, Age1, Age2).