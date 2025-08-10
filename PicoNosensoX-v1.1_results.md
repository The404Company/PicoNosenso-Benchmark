# FINAL BENCHMARK REPORT

Benchmark for 10 (`0.1` to `1.0`) temperatures with 5 runs each.

Total questions per run: `200`

## Temperature: 0.1
| Run | Accuracy |
|-----|----------|
| 1   | 2.0%     |
| 2   | 2.0%     |
| 3   | 2.0%     |
| 4   | 1.5%     |
| 5   | 0.5%     |

- **Average**: 1.6%
- **Min/Max**: 0.5%/2.0%

## Temperature: 0.2
| Run | Accuracy |
|-----|----------|
| 1   | 2.5%     |
| 2   | 0.5%     |
| 3   | 1.5%     |
| 4   | 1.5%     |
| 5   | 3.0%     |

- **Average**: 1.8%
- **Min/Max**: 0.5%/3.0%

## Temperature: 0.3
| Run | Accuracy |
|-----|----------|
| 1   | 1.0%     |
| 2   | 2.0%     |
| 3   | 1.5%     |
| 4   | 2.0%     |
| 5   | 2.0%     |

- **Average**: 1.7%
- **Min/Max**: 1.0%/2.0%

## Temperature: 0.4
| Run | Accuracy |
|-----|----------|
| 1   | 0.5%     |
| 2   | 1.5%     |
| 3   | 2.5%     |
| 4   | 2.0%     |
| 5   | 2.0%     |

- **Average**: 1.7%
- **Min/Max**: 0.5%/2.5%

## Temperature: 0.5
| Run | Accuracy |
|-----|----------|
| 1   | 2.5%     |
| 2   | 2.0%     |
| 3   | 1.5%     |
| 4   | 1.0%     |
| 5   | 2.5%     |

- **Average**: 1.9%
- **Min/Max**: 1.0%/2.5%

## Temperature: 0.6
| Run | Accuracy |
|-----|----------|
| 1   | 1.5%     |
| 2   | 2.5%     |
| 3   | 0.5%     |
| 4   | 2.5%     |
| 5   | 2.5%     |

- **Average**: 1.9%
- **Min/Max**: 0.5%/2.5%

## Temperature: 0.7
| Run | Accuracy |
|-----|----------|
| 1   | 2.5%     |
| 2   | 4.5%     |
| 3   | 1.0%     |
| 4   | 2.0%     |
| 5   | 1.5%     |

- **Average**: 2.3%
- **Min/Max**: 1.0%/4.5%

## Temperature: 0.8
| Run | Accuracy |
|-----|----------|
| 1   | 3.0%     |
| 2   | 2.5%     |
| 3   | 3.5%     |
| 4   | 4.0%     |
| 5   | 1.0%     |

- **Average**: 2.8%
- **Min/Max**: 1.0%/4.0%

## Temperature: 0.9
| Run | Accuracy |
|-----|----------|
| 1   | 1.5%     |
| 2   | 1.5%     |
| 3   | 3.5%     |
| 4   | 1.5%     |
| 5   | 2.0%     |

- **Average**: 2.0%
- **Min/Max**: 1.5%/3.5%

## Temperature: 1.0
| Run | Accuracy |
|-----|----------|
| 1   | 1.5%     |
| 2   | 2.0%     |
| 3   | 2.0%     |
| 4   | 0.0%     |
| 5   | 2.5%     |

- **Average**: 1.6%
- **Min/Max**: 0.0%/2.5%

> **OPTIMAL TEMPERATURE: 0.8 with 2.8% average accuracy**. That's what the benchmark says. In actual use, 0.6 or 0.7 is still heaviely reccomended.

## Interference parameters
```
max_length=256,
temperature=temperature,
repetition_penalty=1.2,
do_sample=True
```
