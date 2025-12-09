Here is your cheatsheet rewritten cleanly in **markdown format**, ready to copy into notes/Notion/Obsidian:

---

# 📘 Hypothesis Testing & ANOVA Cheatsheet

---

## ## 1. **One-Sample Mean Test**

*Assume normal distribution*

---

### **Case A — Population variance σ² known**

**Hypotheses**

* H₀: μ = μ₀
* H₁: μ ≠ μ₀ (or one-sided)

**Test Statistic**

```math
Z = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}}
```

**Decision Rule**

* Reject H₀ if (|Z| > Z_{\alpha/2})

---

### **Case B — Population variance σ² unknown (t-test)**

```math
t = \frac{\bar{X} - \mu_0}{s/\sqrt{n}}
```

* df = (n - 1)
* Reject H₀ if (|t| > t_{\alpha/2, n-1})

---

---

# ## 2. **Two-Sample Mean Tests (Independent Samples)**

---

### **A. σ₁, σ₂ known**

```math
Z = \frac{(\bar{X}_1 - \bar{X}_2) - (\mu_1 - \mu_2)_0}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}
```

---

### **B. σ₁, σ₂ unknown — Large samples (n ≥ 30)**

```math
Z = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}
```

---

### **C. σ₁, σ₂ unknown — Small samples, equal variances (Pooled t-test)**

**Pooled Variance**

```math
s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}
```

**Test Statistic**

```math
t = \frac{\bar{X}_1 - \bar{X}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}
```

* df = (n_1 + n_2 - 2)

---

---

# ## 3. **Single-Factor ANOVA (Completely Randomized Design)**

*Model:*

```math
Y_{ij} = \mu + \tau_i + \epsilon_{ij}
```

* (i = 1,…,a) groups
* (j = 1,…,n) observations per group

**Hypotheses**

* H₀: μ₁ = μ₂ = … = μₐ
* H₁: At least one mean differs

---

## **Sums of Squares**

### **Treatment (Between Groups)**

```math
SS_{Trement} = n \sum_{i=1}^a (\bar{Y}_i - \bar{Y})^2
```

### **Error (Within Groups)**

```math
SS_E = \sum_{i=1}^a \sum_{j=1}^n (Y_{ij} - \bar{Y}_i)^2
```

### **Total**

```math
SS_{Total} = SS_{Treatment} + SS_E
```

---

## **Degrees of Freedom**

* Treatment: (a - 1)
* Error: N - a = a(n - 1)
* Total: (N - 1)

---

## **Mean Squares**

```math
MS_{Treatment} = \frac{SS_{Treatment}}{a - 1}
```

```math
MS_E = \frac{SS_E}{N - a}
```

---

## **F Statistic**

```math
F_0 = \frac{MS_{Treatment}}{MS_E}
```

**Decision Rule**
Reject H₀ if:

```math
F_0 > F_{\alpha,a-1,N-a}
```

