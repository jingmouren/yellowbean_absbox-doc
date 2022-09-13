test01 = Generic(
    "TEST01"
    ,("2021-03-01","2021-06-15","2021-07-26")
    ,{"payment":"Monthly","collection":"Monthly"}
    ,{'breakdown':[["Mortgage"
        ,{"faceValue":120,"originRate":["Fix",0.045],"originTerm":30
          ,"frequency":"Monthly","originDate":"2021-02-01"}
          ,{"currentBalance":120
          ,"currentRate":0.08
          ,"remainTerms":20
          ,"status":"current"}]]}
    ,(("acc01",{"balance":0}),)
    ,(("A1",{"balance":100
             ,"rate":0.07
             ,"originBalance":100
             ,"originRate":0.07
             ,"startDate":"2020-01-03"
             ,"rateType":{"Fix":0.08}
             ,"bondType":{"Sequential":None}})
      ,("B",{"balance":20
             ,"rate":0.0
             ,"originBalance":100
             ,"originRate":0.07
             ,"startDate":"2020-01-03"
             ,"rateType":{"Fix":0.00}
             ,"bondType":{"Equity":None}
             }))
    ,(("trusteeFee",{"type":{"FixFee":30}}),)
    ,{"Normal":[
         ["PayFee",["acc01"],['trusteeFee']]
         ,["PayInt","acc01",["A1"]]
         ,["PayPrin","acc01",["A1"]]
         ,["PayPrin","acc01",["B"]]
         ,["PayEquityResidual","acc01","B"]
     ]}
    ,(["CollectedInterest","acc01"]
      ,["CollectedPrincipal","acc01"]
      ,["CollectedPrepayment","acc01"]
      ,["CollectedRecoveries","acc01"])
    ,None)