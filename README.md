# 🛒 E-commerce Test Automation Framework

[![CI](https://github.com/Marisa-GIT/Third-Project-Professional-E-commerce-Framework/actions/workflows/automation.yml/badge.svg)](
https://github.com/Marisa-GIT/Third-Project-Professional-E-commerce-Framework/actions/workflows/automation.yml
)

A professional Selenium automation framework built with **Python**, **Pytest**, and the **Page Object Model (POM)** following clean architecture and object-oriented design principles.

---

## 📌 Features

- Selenium WebDriver
- Python + Pytest
- Page Object Model (POM)
- Driver Factory Pattern
- Reusable BasePage
- Centralized Locators
- JSON Test Data Management
- Data-Driven Testing
- Logging System
- Automatic Screenshots on Failure
- GitHub Actions CI
- Cross-browser support (Chrome, Firefox, Edge)

---

## 🏗️ Project Structure

```
E-commerce Framework
│
├── .github/
│   └── workflows/
│       └── automation.yml
│
├── config/
│   ├── browsers.py
│   └── settings.py
│
├── core/
│   ├── base_page.py
│   ├── driver_factory.py
│   └── logger.py
│
├── data/
│   ├── products.json
│   └── users.json
│
├── locators/
│   ├── cart_locators.py
│   ├── checkout_complete_locators.py
│   ├── checkout_information_locators.py
│   ├── checkout_overview_locators.py
│   ├── inventory_locators.py
│   └── login_locators.py
|
├── logs/
│
├── pages/
│   ├── cart_page.py
│   ├── checkout_complete_page.py
│   ├── checkout_information_page.py
│   ├── checkout_overview_page.py
│   ├── inventory_page.py
│   └── login_page.py
|
├── reports/
├── screenshots/
│
├── tests/
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_end_to_end.py
│   ├── test_inventory.py
│   ├── test_login.py
│   └── 
│
├── utils/
│   └── test_data_manager.py
│
├── conftest.py
├── pytest.ini 
├── README.md
└── requirements.txt

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming language |
| Selenium | Web automation |
| Pytest | Test framework |
| GitHub Actions | Continuous Integration |
| JSON | Test data |
| Allure | Reporting |
| Logging | Execution logs |

---

## 🚀 Implemented Test Scenarios

### Login

- Successful login
- Data-driven login
- Locked user login

### Inventory

- Verify product catalog display
- Sort products by price
- Add product to cart
- Add multiple products
- Verify cart badge updates

### Shopping Cart

- Remove product
- Continue shopping
- Proceed to checkout
- Verify cart badge lifecycle

### Checkout

- First name required validation
- Last name required validation
- Postal code required validation
- Cancel checkout
- Verify checkout summary
- Verify item total
- Verify tax calculation
- Verify total amount
- Complete order

### End-to-End

- Complete purchase
- Purchase multiple products
- Purchase after removing a product
- Complete checkout flow
- Purchase with problem user
- Purchase with performance glitch user

---

## 📊 Framework Architecture

DriverFactory

↓

BasePage

↓

Page Objects

↓

Tests

This architecture keeps responsibilities separated and improves maintainability and scalability.

---

## ▶️ Running the Tests

```bash
pip install -r requirements.txt

pytest -v
```

---

## 🔄 Continuous Integration

GitHub Actions automatically:

- Installs dependencies
- Executes all tests
- Captures screenshots on failures
- Uploads execution artifacts

---

## 📸 Screenshots

Include screenshots of:

- Login
- Inventory
- Cart
- Checkout
- GitHub Actions execution

---

## 📈 Future Improvements

- Docker execution
- Parallel execution with pytest-xdist
- Selenium Grid
- BrowserStack integration
- API + UI hybrid testing
- Database validation
- AI-assisted test generation

---

## 👩‍💻 Author

**Isabel Vides**

QA Automation Engineer

- LinkedIn: www.linkedin.com/in/maria-isabel-vides-021531232
- GitHub: https://github.com/Marisa-GIT