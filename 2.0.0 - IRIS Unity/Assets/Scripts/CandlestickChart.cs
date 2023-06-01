using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CandlestickChart : MonoBehaviour
{
    public float chartWidth = 10f;
    public float chartHeight = 5f;
    public float candleWidth = 0.5f;
    public int numCandle = 0;
    public Sprite candleSprite;

    void Start()
    {
        CreateCandlestick(150f, 170f, 180f, 140f, (candleWidth + 0.15f) * (float)numCandle);  // Example call for a single candlestick
        numCandle++;
        CreateCandlestick(160f, 155f, 170f, 150f, (candleWidth + 0.15f) * (float)numCandle);  // Example call for another candlestick
        // Add more CreateCandlestick() calls here for additional candlesticks
    }

    void CreateCandlestick(float openPrice, float closePrice, float highPrice, float lowPrice, float num)
    {
        // Calculate the vertical scaling factor for the chart
        float minPrice = Mathf.Min(openPrice, closePrice, highPrice, lowPrice);
        float maxPrice = Mathf.Max(openPrice, closePrice, highPrice, lowPrice);
        float priceRange = maxPrice - minPrice;
        float verticalScale = chartHeight / priceRange;

        // Create a GameObject to represent the candlestick
        GameObject candlestick = new GameObject("Candlestick");
        candlestick.transform.SetParent(transform);

        // Set the position and size of the candlestick
        candlestick.transform.localPosition = new Vector3(chartWidth / 2f + num, (openPrice - minPrice) * verticalScale / 2f, 0f);
        candlestick.transform.localScale = new Vector3(candleWidth, (closePrice - openPrice) * verticalScale, 1f);

        // Create a sprite renderer to render the candlestick
        SpriteRenderer spriteRenderer = candlestick.AddComponent<SpriteRenderer>();
        spriteRenderer.sprite = candleSprite;
        spriteRenderer.color = (closePrice > openPrice) ? Color.green : Color.red;

        // Create a line renderer to render the high-low range of the candlestick
        LineRenderer lineRenderer = candlestick.AddComponent<LineRenderer>();
        lineRenderer.positionCount = 2;
        lineRenderer.startWidth = 0.02f;
        lineRenderer.endWidth = 0.02f;
        lineRenderer.SetPosition(0, new Vector3(chartWidth / 2f + num, (highPrice - minPrice) * verticalScale / 2f, 0f));
        lineRenderer.SetPosition(1, new Vector3(chartWidth / 2f + num, (lowPrice - minPrice) * verticalScale / 2f, 0f));
        lineRenderer.material = new Material(Shader.Find("Sprites/Default"));
        lineRenderer.startColor = (closePrice > openPrice) ? Color.green : Color.red;
        lineRenderer.endColor = (closePrice > openPrice) ? Color.green : Color.red;
    }
}
