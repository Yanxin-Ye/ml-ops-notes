
## Construct a Simpson’s Paradox

**Where T wins in both subgroups, but loses to C when aggregated**

---

### **Step 1 — Create 2 subgroups with very different baselines**

* **Group A:** 20% (high)
* **Group B:** 5% (low)

---

### **Step 2 — Make T win slightly in both groups**

|       | **A**     | **B**    |
| ----- | --------- | -------- |
| **T** | **22%** ✓ | **6%** ✓ |
| **C** | 20%       | 5%       |

---

### **Step 3 — Give T most of the traffic in low group B**

### **Give C most of the traffic in high group A**

> So **T sees low-base users mostly**

---

|       | **A**                  | **B**                 | **Total**                     |
| ----- | ---------------------- | --------------------- | ----------------------------- |
| **T** | 22% ✓  <br> 220 / 1000 | 6% ✓  <br> 540 / 9000 | **7.6%** ✗ <br> 760 / 10000   |
| **C** | 20% <br> 1800 / 9000   | 5% <br> 50 / 1000     | **18.5%** ✓ <br> 1850 / 10000 |

---

### **Result**

* T wins in **Group A**
* T wins in **Group B**
* **C wins overall** ← Simpson’s Paradox

---

### **Core Idea**

Overall rate is a **weighted average**.
Even if T is better in each subgroup, it can lose overall if:

* T gets more traffic from **low-performing users**
* C gets more traffic from **high-performing users**
