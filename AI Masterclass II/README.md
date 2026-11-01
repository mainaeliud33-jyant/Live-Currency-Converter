# Nakuru Dairy Co-op montly Milk Collection analyzer

## What it Does
* Consolidates farmer profile registration sheets with raw volume logs.
* Aggregates total metrics to compute overall zonal production performance.
* Identifies the single top-volume milk supplier per physical area to manage performance tracking.
* Prints a polished summary view tailored for direct management evaluation distributions.

## 2. Why does it exist?
In local dairy operations, processing hundreds of daily physical milk drop receipts manually creates significant overhead and human entry risk. 
i built this tool to:
* **Eliminate Manual Math:** Fully automate zonal aggregation calculations, reducing accounting error risks for the management team.
* **Accelerate Business Insights:** Instantly extract operational intelligence—such as total monthly regional supply trends and identifying top-tier suppliers—to help managers make faster supply chain decisions.
* **Standardise Formats:** Transform messy data inputs into clean,  executive reporting tables optimized for financial audits and stakeholder updates.

## 3. How do you run it?
Ensure you have the following software:
* **Python
* **pandas

### Setup and Execution Step-by-Step

1. **download the project files** into a local working directory on your computer.
2. **Open your system terminal** and change your directory path to your project folder:
   ```bash
   cd path/to/your/project-folder
   ```
3. **Install the dependencies** required to handle the data arrays:
   ```bash
   pip install pandas
   ```
4. **Execute the analysis script**:
   ```bash
   python main.py
   ```

## 4. What does the outcome look like?
When successfully executed, the program processes the data and outputs a highly clean, aligned text table directly inside your terminal interface. 

The output is formatted with currency designators, decimal alignments, and zone metrics, appearing exactly as follows:

```text
===============FINAL END MONTH SUMMARY===============
       total litres   total_payout       top_farmer
zone                                               
Bahati    1,852.1 L   KES83,344.50  Timothy Kariuki
Molo      2,035.5 L  KES122,130.00     James Mbugua
Njoro       834.4 L   KES39,216.80      Simon Kamau
======================================================
```