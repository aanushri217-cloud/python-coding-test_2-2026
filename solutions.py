'''
❗ Q1: Workforce Stability Index

A company tracks employees across multiple projects over time. Each project assigns a performance score, but employees may appear multiple times in different projects and months.

You must compute a stability index for each employee based on their performance consistency and return a ranked list of employees.

 Q2: Fraud Pattern Detection Engine

A banking system records transaction logs for multiple users over time.

Each user may perform multiple transactions in a day. Some patterns indicate suspicious behavior based on frequency and repetition trends.

Your task is to analyze the dataset and classify users into normal or suspicious categories.
 Q3: Smart Inventory Drift Analyzer

A warehouse system logs continuous stock movements including additions, removals, and corrections.

Due to system delays, logs may not be in chronological order.

Your task is to determine the final correct inventory state and detect inconsistencies in movement patterns.

 Q4: Customer Engagement Ranking System

A digital platform tracks different types of user interactions such as clicks, views, purchases, and shares.

Each interaction contributes differently to engagement, and weights may vary over time.

Your task is to compute a dynamic engagement score and generate a sorted ranking of users.

 Q5: Multi-Zone Delivery Feasibility Engine

A logistics company assigns delivery tasks across multiple zones with constraints like time windows, capacity limits, and priority levels.

Not all requests can be fulfilled due to overlapping constraints.

Your task is to determine which deliveries can be successfully completed and which must be rejected.
'''

Q1. #Sample data format: { employee_id: [performance_scores]}
    workforce_data = {
        "EMP001": [85, 88, 84, 86]
        "EMP002": [95, 60, 90, 55]
        "EMP003": [70, 72, 71, 73]

    }

    stability_indices = {}

    for emp_id, scores in workforce_data.items():
        if not scores:
            stability_indices[emp_id] = 0
            continue

        total = 0
        for s in scores:
            total += s
        average = total / len(scores)

        variance_sum = 0
        for s in scores:
            variance_sum += (s - average) ** 2
        variance = variance_sum / len(scores)

        stability_index = 100 / (1 + variance)
        stability_indices[emp_id] = round(stability_index, 2)

    print("Workforce Stability Index:", stability_indices)


2. 
   transactions = [
       ("user_A", "day1", 500),
       ("user_B", "day1", 10000),
       ("user_A", "day1", 50),
       ("user_A", "day1", 20),
       ("user_A", "day1", 10),
   ]

   MAX_TX_PER_DAY = 3
   MAX_TX_AMOUNT = 5000

   user_behaviour = {}
   suspicious_users = set()

   for user, day, amount in transactions:
    if amount > MAX_TX_AMOUNT:
       suspicious_users.add(user)

    if user not in user_behaviour:
       user_behaviour[user] = {}
    if day not in user_behaviour[user]:
       user_behaviour[user][day] = 0

    user_behaviour[user][day] += 1
    if user_behaviour[user][day] > MAX_TX_PER_DAY:
       suspicious_users.add(user)

   classifications = {}
   for user in user_behaviour.keys():
       if user in suspicious_users:
          classifications[user] = "suspicious"
       else:
          classifications[user] = "normal"

   print("User Classifications:", classifications)

Q3. 
    inventory_logs = [
       (10, "addition", 20)
       (5, "addition", 50)
       (15, "removal", 10)
       (20, "correction", 55)
    ]
    
    inventory_logs.sort(key = lambda x: x[0])

    current_stock = 0

    for timestamp, op, qty in inventory_logs:
        if op == "addition":
           current_stock += qty
        elif op == "removal":
           current_stock -= qty
        elif op == "correction":
           current_stock = qty

    print("Final correct inventory state:", current_stock)

