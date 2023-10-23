Reference
=================

Asset Cashflow Projection Document
-----------------------------------

Performing Asset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mortgage/Loan/Installment
"""""""""""""""""""""""""""

* determine the ``projection dates``
  
  * ``start date`` -> There is a field in asset present the `origination date` ,which means the date when asset came into existance.
  * ``(original/scheduled) payment dates`` -> Then, cashflow engine will generate a vector of payment dates bases on `origination date` and `payment frequency`
  * ``remaining payment dates`` -> base on the input field `remaining terms`, engine will trancate the `payment dates` to get `remaining payment dates`

* project cashflow with assumptions
  
  * ``projected cashflow`` -> Given `remaining payment dates` and `current balance` , then engine will calculate cashflow with assumption starting from `remaining payment dates`

* truncate the cashflow via `cutoff date`

  * `projected cashflow` was truncated via `cutoff date` ,that's the cashflow of asset which flows into the SPV

Non-Performing Asset(WIP)
""""""""""""""""""""""

Why Mortgage Performance Assumption is so complex ?
----------------------------------------

Before version ``0.21.x`` , pool performance assumption is just a *LIST*, which includes like ``{"CDR":0.05}``

But it is not scalable when more types of assets and assumptions are introduced. for example: when including new assumption on *Delinquency*, what happen if user passes ``[{"CDR":0.05},{"Delinquency":0.05}]`` ? How delinquency interacts with default assumption ? 

It can be solved by introducing "How" via supplying a *Tuple* as below :

.. code-block:: python
  
  ("Mortgage","Delinq",<delinquency assump>,<prepay assump>,<recovery assump>,<extra assump>)

With starting ``("Mortgage","Delinq",...)`` the engine treat this as identifier to logic of how apply pool assumption.

It is scalable if more assumption type comming in.


Why so many list tuples and maps in deal model
---------------------------------------------------

* Unlike `Class` , all data were exposed to user via native structure, transperancy matters.
  
  `Class` will hide `states` and changing behavior of methods, that's dark magic we should avoid.

* Because native stucture will enable user's own way to build data structure required.
  
  User has his/her own code base, which may have heavily couple with `PyDantic` or `Numpy` or other library, but anyway, all these data structure will provide methods to convert back to Python structure.

* Most of persistent layer supports native structure, like `PyMongo` `redis` etc . It's easy to pull from these data and initialized models.


* Isn't making too much keystroke to model a deal ? 

  Don't have to that way ,because `list` `tuple` `maps` are just *DATA* ,user can easily build candy function wrap the generator 

  .. code-block:: python 

  ["payPrin","SourceAccount","A"
          ,{"formula": ("substract"
                          ,("poolBalance",)
                          ,("factor"
                              ,("poolBalance",), 0.12))}]
  # isn't it nice ?
  
  def payBondwithOC(an,bn,oc):
      return ["payPrin",an,bn
                        ,{"formula": ("substract"
                                        ,("poolBalance",)
                                        ,("factor"
                                            ,("poolBalance",),oc))}]

JSON Format
--------------

Deal 
^^^^^^^^
A deal object can be converted into json format via a property field `.json`

.. code-block:: python
   
   #Assuming 

   test.json  

   #{'tag': 'MDeal',
   # 'contents': {'dates': {'tag': 'PreClosingDates',
   #   'contents': ['2021-03-01',
   #    '2021-06-15',
   #    None,
   #    '2030-01-01',
   #    ['2021-06-15', {'tag': 'MonthEnd'}],
   #    ['2021-07-26', {'tag': 'DayOfMonth', 'contents': 20}]]},
   #  'name': 'Multiple Waterfall',
   #  'status': {'tag': 'Amortizing'},
   #  'pool': {'assets': [{'tag': 'Mortgage',
   #     'contents': [{'originBalanc

