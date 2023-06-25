from absbox.local.generic import Generic

test01 = Generic(
    "liquidation provider with interest"
    ,{"cutoff":"2021-03-01","closing":"2021-06-15","firstPay":"2021-07-26"
     ,"payFreq":["DayOfMonth",20],"poolFreq":"MonthEnd","stated":"2030-01-01"}
    ,{'assets':[["Mortgage"
        ,{"originBalance":2200,"originRate":["fix",0.045],"originTerm":30
          ,"freq":"Monthly","type":"Level","originDate":"2021-02-01"}
          ,{"currentBalance":1200
          ,"currentRate":0.08
          ,"remainTerm":20
          ,"status":"current"}]]}
    ,(("acc01",{"balance":0}),("acc02",{"balance":0}))
    ,(("A1",{"balance":1000
             ,"rate":0.08
             ,"originBalance":1000
             ,"originRate":0.08
             ,"startDate":"2020-01-03"
             ,"rateType":{"Fixed":0.09}
             ,"bondType":{"Sequential":None}})
      ,("B",{"balance":500
             ,"rate":0.05
             ,"originBalance":500
             ,"originRate":0.05
             ,"startDate":"2020-01-03"
             ,"rateType":{"Fixed":0.10}
             ,"bondType":{"Sequential":None}
             }))
    ,tuple()
    ,{"amortizing":[
         ["calcInt","A1"]
         ,["liqSupport", "insuranceProvider","acc01"
           ,("Max"
             ,("substract",("bondDueInt","A1","B"),("accountBalance","acc01"))
             ,("constant",0.0)
            )]
         ,["accrueAndPayInt","acc01",["A1","B"]]
         ,["payPrin","acc02",["A1"]]
         ,["payPrin","acc02",["B"]]
         ,["If"
           ,[("bondBalance","A1","B"),"=",0]
           ,["accrueAndPayInt","acc02",["A1","B"]]
           ,["liqRepay","bal","acc01","insuranceProvider"]
           ,["liqRepay","bal","acc02","insuranceProvider"]]
     ]}
    ,[["CollectedInterest","acc01"]
      ,["CollectedPrincipal","acc02"]
      ,["CollectedPrepayment","acc02"]
      ,["CollectedRecoveries","acc02"]]
    ,{"insuranceProvider":
         {"lineOfCredit":100,"start":"2021-06-15"
          ,"type":{"Reset":"MonthEnd","Formula":("bondBalance",),"Pct":0.0015}}
     })
