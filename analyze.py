from pathlib import Path
import pandas as pd
root=Path(__file__).parent
df=pd.read_csv(root/'data/consolidated_financials_krw_million.csv')
df['revenue_growth_pct']=df['revenue'].pct_change()*100
df['gross_margin_pct']=df['gross_profit']/df['revenue']*100
df['operating_margin_pct']=df['operating_profit']/df['revenue']*100
df['net_margin_pct']=df['net_income']/df['revenue']*100
df['current_ratio_pct']=df['current_assets']/df['current_liabilities']*100
df['debt_to_equity_pct']=df['total_liabilities']/df['equity']*100
df['equity_ratio_pct']=df['equity']/df['total_assets']*100
df['interest_bearing_debt']=df['short_debt']+df['long_debt']
df['net_debt_cash_only']=df['interest_bearing_debt']-df['cash']
df['capex_total']=df['ppe_capex']+df['intangible_capex']
df['fcf_cfo_minus_capex']=df['cfo']-df['capex_total']
df['cfo_to_net_income_pct']=df['cfo']/df['net_income']*100
df['avg_assets']=(df['total_assets']+df['total_assets'].shift())/2
df['avg_equity']=(df['equity']+df['equity'].shift())/2
df['roa_pct']=df['net_income']/df['avg_assets']*100
df['roe_pct']=df['parent_net_income']/df['avg_equity']*100
df.to_csv(root/'data/financial_ratios.csv',index=False)
print(df[['year','revenue_growth_pct','operating_margin_pct','current_ratio_pct','debt_to_equity_pct','fcf_cfo_minus_capex']].to_string(index=False))
