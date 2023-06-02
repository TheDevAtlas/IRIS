using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using UnityEngine.Networking;
using System;

public class StockData : MonoBehaviour
{
    private const string URL = "https://query1.finance.yahoo.com/v8/finance/chart/AAPL?interval=1d";

    void Start()
    {
        StartCoroutine(FetchStockData());
    }

    IEnumerator FetchStockData()
    {
        UnityWebRequest request = UnityWebRequest.Get(URL);
        yield return request.SendWebRequest();

        if (request.result != UnityWebRequest.Result.Success)
        {
            Debug.LogError("Failed to fetch stock data: " + request.error);
            yield break;
        }

        string json = request.downloadHandler.text;
        StockDataResponse response = JsonUtility.FromJson<StockDataResponse>(json);

        if (response.chart != null && response.chart.result.Count > 0)
        {
            ChartResult result = response.chart.result[0];
            List<long> timestamps = result.timestamp;
            List<double> closingPrices = result.indicators.quote[0].close;

            // Assuming both lists have the same count, we can iterate over one of them
            for (int i = 0; i < timestamps.Count; i++)
            {
                DateTime date = UnixTimeStampToDateTime(timestamps[i]);
                double closingPrice = closingPrices[i];

                Debug.Log("Date: " + date.ToString("yyyy-MM-dd") + ", Closing Price: " + closingPrice);
            }
        }
    }

    // Helper method to convert Unix timestamp to DateTime
    private DateTime UnixTimeStampToDateTime(long unixTimeStamp)
    {
        DateTime dateTime = new DateTime(1970, 1, 1, 0, 0, 0, 0, DateTimeKind.Utc);
        dateTime = dateTime.AddSeconds(unixTimeStamp).ToLocalTime();
        return dateTime;
    }

    // Classes for deserializing JSON response
    [Serializable]
    public class StockDataResponse
    {
        public Chart chart;
    }

    [Serializable]
    public class Chart
    {
        public List<ChartResult> result;
    }

    [Serializable]
    public class ChartResult
    {
        public List<long> timestamp;
        public Indicators indicators;
    }

    [Serializable]
    public class Indicators
    {
        public List<Quote> quote;
    }

    [Serializable]
    public class Quote
    {
        public List<double> close;
    }
}
