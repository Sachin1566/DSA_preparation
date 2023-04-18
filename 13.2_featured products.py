
from collections import Counter
products=['yellowshirt','redhat','blackshirt','bluepants','redhat','pinkpant','yellowshirt','greenpant','greenpant','greenpant']
products_count=dict(Counter(products))
print("given products are\n",products_count)

max=0
req_product=[]

# find freency of product
for i in products_count:
    if max<products_count[i]:
            max=products_count[i]
            
            
for key,value in products_count.items():
    if max==value:
        req_product.append(key)
        # req_product.append(value) 


print(req_product[-1])