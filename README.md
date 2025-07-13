# PicoNosenso-Benchmark
A Benchmark to test our PicoNosenso-series models on various trivia questions.


# FINAL BENCHMARK REPORT [PicoNosenso-v1](https://huggingface.co/Lominub44/PicoNosenso-v1)

Benchmark for 10 (`0.1` to `1.0`) temperatures with 5 runs each.

Total questions per run: `200`

## Temperature: 0.1
| Run | Accuracy |
|-----|----------|
| 1   | 15.0%    |
| 2   | 13.0%    |
| 3   | 17.0%    |
| 4   | 16.5%    |
| 5   | 15.0%    |

- **Average**: 15.3%
- **Min/Max**: 13.0%/17.0%

## Temperature: 0.2
| Run | Accuracy |
|-----|----------|
| 1   | 15.0%    |
| 2   | 16.0%    |
| 3   | 15.0%    |
| 4   | 14.5%    |
| 5   | 14.5%    |

- **Average**: 15.0%
- **Min/Max**: 14.5%/16.0%

## Temperature: 0.3
| Run | Accuracy |
|-----|----------|
| 1   | 12.5%    |
| 2   | 16.0%    |
| 3   | 16.5%    |
| 4   | 18.5%    |
| 5   | 15.0%    |

- **Average**: 15.7%
- **Min/Max**: 12.5%/18.5%

## Temperature: 0.4
| Run | Accuracy |
|-----|----------|
| 1   | 17.0%    |
| 2   | 16.5%    |
| 3   | 15.5%    |
| 4   | 18.0%    |
| 5   | 12.0%    |

- **Average**: 15.8%
- **Min/Max**: 12.0%/18.0%

## Temperature: 0.5
| Run | Accuracy |
|-----|----------|
| 1   | 14.5%    |
| 2   | 16.0%    |
| 3   | 16.5%    |
| 4   | 15.0%    |
| 5   | 17.0%    |

- **Average**: 15.8%
- **Min/Max**: 14.5%/17.0%

## Temperature: 0.6
| Run | Accuracy |
|-----|----------|
| 1   | 17.0%    |
| 2   | 19.5%    |
| 3   | 15.5%    |
| 4   | 18.0%    |
| 5   | 16.5%    |

- **Average**: 17.3%
- **Min/Max**: 15.5%/19.5%

## Temperature: 0.7
| Run | Accuracy |
|-----|----------|
| 1   | 17.0%    |
| 2   | 19.0%    |
| 3   | 15.5%    |
| 4   | 15.5%    |
| 5   | 16.5%    |

- **Average**: 16.7%
- **Min/Max**: 15.5%/19.0%

## Temperature: 0.8
| Run | Accuracy |
|-----|----------|
| 1   | 11.5%    |
| 2   | 17.0%    |
| 3   | 15.0%    |
| 4   | 14.0%    |
| 5   | 17.5%    |

- **Average**: 15.0%
- **Min/Max**: 11.5%/17.5%

## Temperature: 0.9
| Run | Accuracy |
|-----|----------|
| 1   | 14.5%    |
| 2   | 15.5%    |
| 3   | 16.0%    |
| 4   | 16.0%    |
| 5   | 18.5%    |

- **Average**: 16.1%
- **Min/Max**: 14.5%/18.5%

## Temperature: 1.0
| Run | Accuracy |
|-----|----------|
| 1   | 11.5%    |
| 2   | 15.0%    |
| 3   | 15.5%    |
| 4   | 16.5%    |
| 5   | 16.0%    |

- **Average**: 14.9%
- **Min/Max**: 11.5%/16.5%

> **OPTIMAL TEMPERATURE: 0.6 with 17.3% average accuracy**

## Interference parameters
```
max_length=256,
temperature=temperature,
repetition_penalty=1.2,
do_sample=True
```
