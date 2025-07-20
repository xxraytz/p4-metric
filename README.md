# Harmonic Averaging in Classifier Quality Assessment

[Python](https://pypi.org/project/p4-metric)

[License](LICENSE)

This repo implements the **P4** metric introduced in  
O. Seredin & A. Kopylov, “Harmonic Averaging in Classifier Quality Assessment,”  
*Pattern Recognition and Image Analysis*, 34 (4) 1160‑1171 (2024)  
<https://link.springer.com/article/10.1134/S1054661824701220>.

The metric is the harmonic mean of *precision* and *recall*:  
- **Binary:** compute it twice—once with each class as the positive class.
- **Multiclass:** apply the same principle using **One‑Vs‑Rest** aggregation.

**Key properties**

* handles class imbalance without arbitrary weights;  
* treats all classes symmetrically (no privileged positive class);  

---

## Installation

```bash
pip install p4-metric
```

Supported Python ≥ 3.9.  
`numpy` and `scipy ≥ 1.11` are pulled automatically.

---

## Quick start

```python
import numpy as np
from p4metric import p4_metric

cm = np.array([[50,  2,  3],
               [ 4, 45,  5],
               [ 1,  2, 40]])

score = p4_metric(cm)
print(f"P4 metric: {score:.4f}")   # → 0.9146
```

---

## Citation

If you use `p4-metric` in academic work, please cite the original article:

```bibtex
@article{seredin2024harmonic,
  title={Harmonic Averaging in Classifier Quality Assessment},
  author={Seredin, OS and Kopylov, AV},
  journal={Pattern Recognition and Image Analysis},
  volume={34},
  number={4},
  pages={1160--1171},
  year={2024},
  publisher={Springer}
}
```

---

## License

This project is distributed under the **MIT License**.  
© 2024 Oleg Seredin & Andrei Kopylov.
