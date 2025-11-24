import statistics as st

def basic_stats(data):
    return {
        "mean": st.mean(data),
        "median": st.median(data),
        "variance": st.variance(data)
    }

if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5]
    print(basic_stats(sample))
