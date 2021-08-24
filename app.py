import numpy as np
import pandas as pd
from collections import defaultdict
from numpy import seterr
###
res=pd.read_csv('trip_tage_final.csv')
###

###
Lawrence_ratings = [
            {'name':'龐家肉羹', 'rating':4.9},
            {'name':'1010湘-南港中信店', 'rating':2},
            {'name':'龜山島阿興現撈海產店', 'rating':2},
            {'name':'1+1創意廚房', 'rating':2}
         ]
###
Lawrence_ratings = pd.DataFrame(Lawrence_ratings)
Lawrence_Id = res[res['name'].isin(Lawrence_ratings['name'])]
Lawrence_ratings=pd.merge(Lawrence_Id, Lawrence_ratings)
Lawrence_ratings=Lawrence_ratings[['_id','name','rating']]
r1=res.copy()
r1=r1[['_id','finalsc','food','serv','cp','atmosphere','亞洲料理','中式料理','台灣小吃','台菜','日式料理','咖啡廳','義式料理','美式料理','海鮮','酒吧','多國料理','牛排','提供素食選擇','燒烤','提供純素選擇','壽司','泰式料理','法式料理','烤肉','歐式料理','韓式料理']]
Lawrence_Id = res[res['name'].isin(Lawrence_ratings['name'])]
Lawrence_ratings=pd.merge(Lawrence_Id, Lawrence_ratings)
Lawrence_ratings=Lawrence_ratings[['_id','name','rating']]
Lawrence_genres_df = r1[r1._id.isin(Lawrence_ratings._id)]
ll1=Lawrence_genres_df.copy(deep=True)
ll1.reset_index(drop=True, inplace=True)

ll1.drop(['finalsc','finalsc','food','serv','cp','atmosphere'], axis=1, inplace=True)
ll1.drop(['_id'], axis=1, inplace=True)
res__profile=ll1.T.dot(Lawrence_ratings.rating)
r2=res.copy()
Lawrence_genres_df = r2.set_index(res._id)
Lawrence_genres_df.drop(['_id','id','name','url','rank','add','phone','phone','price','type','finalsc','food','serv','cp','atmosphere'], axis=1, inplace=True)
recommendation_table_df=(Lawrence_genres_df.dot(res__profile)) / res__profile.sum()
recommendation_table_df.sort_values(ascending=False, inplace=True)
copy = res.copy(deep=True)
copy = copy.set_index('_id', drop=True)
top_20_index = recommendation_table_df.index[:20].tolist()
recommended_res = copy.loc[top_20_index, :]

# Now we can display the top 20 movies in descending order of preference
recommended_res
