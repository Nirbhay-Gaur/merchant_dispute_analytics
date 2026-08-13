# Data Dictionary

| Table          | Column              | Type      | Description                                        |
| -------------- | ------------------- | --------- | -------------------------------------------------- |
| `transactions` | `transaction_id`    | STRING    | Unique ID per transaction                          |
| `transactions` | `merchant_id`       | STRING    | Foreign key to merchant                            |
| `transactions` | `transaction_date`  | DATE      | When the transaction occurred                      |
| `transactions` | `amount`            | FLOAT     | Transaction value                                  |
| `transactions` | `merchant_segment`  | STRING    | Retail / Digital / Restaurant / Travel / Services  |
| `transactions` | `channel`           | STRING    | E-commerce / Card Present / Mobile                 |
| `transactions` | `customer_segment`  | STRING    | Mass / Premium / Small Business                    |
| `disputes`     | `dispute_id`        | STRING    | Unique dispute ID                                  |
| `disputes`     | `transaction_id`    | STRING    | Foreign key to the disputed transaction            |
| `disputes`     | `dispute_date`      | DATE      | When the dispute was opened                        |
| `disputes`     | `dispute_reason`    | STRING    | Fraud / Billing Error / Goods Not Received / Other |
| `disputes`     | `dispute_amount`    | FLOAT     | Amount disputed                                    |
| `disputes`     | `response_days`     | INT       | Number of days the merchant took to respond        |
| `disputes`     | `merchant_won`      | INT (0/1) | 1 = merchant won; 0 = merchant lost                |
| `disputes`     | `chargeback_amount` | FLOAT     | Amount actually charged back                       |
