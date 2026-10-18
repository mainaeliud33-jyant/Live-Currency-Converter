# Live Currency Converter

**Live Currency Converter** is a single-page web application that fetches real-time financial data to display exact conversion rates between major global currencies. 

Currency values shift rapidly due to shifting international market conditions. This application provides a lightweight, front-end solution to quickly track conversion rates without heavy backend requirements or continuous page reloads. It serves as an intuitive interface for assessing instant financial valuations.

## Core Features
* **Public API Integration:** Utilizes `async/await` and the `fetch()` API to retrieve live exchange metrics securely.
* **No Authentication Barrier:** Built using a public endpoint (`er-api.com`) requiring zero complex environment configurations or API keys.
* **Asynchronous Loading States:** Prompts users with a clear visual fallback message while background data transfers complete.
* **Integrated Error Handling:** Explicitly flags structural API failures or network problems to help ensure reliable user troubleshooting.

---

## How to Run It

### Prerequisites
* A standard modern web browser (e.g., Google Chrome, Mozilla Firefox, Microsoft Edge, or Safari).

### Local Execution Steps
1. **Save the file:** Copy the provided HTML code block and save it locally on your computer as `index.html`.
2. **Launch the application:** Double-click the saved `index.html` file to instantly open it inside your default web browser. No local web servers or dependencies are required.

---

## Expected Outcome

### 1. Loading State
When the page generates for the first time, or when you click the conversion trigger, the system displays an immediate update window:
```text
⏳ Loading market rates...
```

### 2. Successful Conversion
Once the public server payload returns successfully, the application generates a clean, formatted card highlighting the exact valuation down to four decimal places:
```text
Live Exchange Valuation
1 USD = 129.5000 KES
```

### 3. Error Fallback
Selecting an unmapped option (like the intentional `ERR - Force Error State` dropdown menu field) triggers the integrated catch block, instantly reporting the problem:
```text
Error: Invalid base currency parameters.
```
