CPR Abonnement Integration
**************************
Module that integrates with third party web service from Serviceplatformen.

The functions serve as facades for ease of interaction with Serviceplatformen's 'SF6002 - CPR Abonnement' service.

*In order for this module to interact with Serviceplatformen you need valid 'Invocation context' UUIDs and a certificate.*


The type of operation you want to perform depends on the type of operation that is assigned to the operation parameter key when calling the function.*

pnr_subscription()
----------------------------
*add, or remove a pnr subscription*

pnr_all_subscribed()
----------------------------
*get all subscribed pnrs*

See client_example.py for examples.
