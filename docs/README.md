# BudgetBuddy

A small spending/allowance tracker you run in the terminal. Add transactions,
list and filter them, see your balance, and get a few quick summaries.

## What it does (v1.0)

Run the app and pick a number from the menu:

| Option | What it does |
|---|---|
| 1) Show balance | Your starting balance plus every transaction |
| 2) List transactions | Every transaction with its id and amount |
| 3) Add a transaction | Asks for a description and an amount, then saves it (category is "general") |
| 4) Filter by category | Lists the transactions in one category, e.g. `food` |
| 5) Show the last transaction | The most recent transaction's description |
| 6) Category breakdown | How many transactions are in each category |
| 7) Spending summary | Total spent, number of transactions, and the average amount |
| 8) Account summary | The account name and how many transactions it has |
| 0) Quit | Exits the app |

Your data lives in `data/budgetbuddy.json`, so anything you add is still there
the next time you open the app.

## Run it

```bash
python main.py
```

## Run the tests

```bash
python -m unittest
```

Both commands work from the root of the repo with Python 3, no installs needed.

## How it's laid out

| File | What it does |
|---|---|
| `main.py` | The menu loop you interact with |
| `storage.py` | Loads and saves the JSON data file |
| `features/core.py` | The transactions, the balance, and small helpers |
| `features/reports.py` | Summary reports (the account summary works; the category totals report is not finished yet) |
| `data/budgetbuddy.json` | The transaction history and starting balance |
| `tests/test_core.py` | Unit tests for the balance and adding a transaction |

## Known limitations (not in v1.0)

- The category totals report is still a stub. Tracked in #3, work in PR #4.
- Typing something that isn't a number as the amount in option 3 crashes the app.
- Option 5 crashes if there are no transactions yet.
- Bug reports from our bug bash (#16, #17, #18, #19) are still open. Fixes are in review (PR #20, PR #21) and will ship in a later release.

## Team

- Baknur01
- alperen-erfidan
- NihalSaha

## Contributing

Pick an open Issue, then read `CONTRIBUTING.md` for the branch naming rules and
the Definition of Done every pull request has to meet.
