using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GraphBuilder : MonoBehaviour
{
    public Sprite candleSprite;
    public float candleSeperation;

    public Vector4[] data;

    private void Start()
    {
        CreateNewChart();
    }
    void CreateNewChart()
    {
        float num = 0;
        foreach(Vector4 d in data)
        {
            CreateCandlestick(d.x, d.y, d.z, d.w, num);
            num++;
        }
    }

    void CreateCandlestick(float openPrice, float closePrice, float highPrice, float lowPrice, float num)
    {
        float minPrice = Mathf.Min(openPrice, closePrice, highPrice, lowPrice);
        float maxPrice = Mathf.Max(openPrice, closePrice, highPrice, lowPrice);
        float priceRange = maxPrice - minPrice;
        float verticalScale = transform.localScale.y / priceRange;

        GameObject candlestick = new GameObject("Candlestick");

        float x = transform.localScale.x / data.Length / 2f;
        candlestick.transform.localPosition = new Vector3(num - transform.localScale.x / 2f, (openPrice - minPrice) * verticalScale / 2f, 0f);
        candlestick.transform.localScale = new Vector3(0.2f, (closePrice - openPrice) * verticalScale, 1f);

        SpriteRenderer spriteRenderer = candlestick.AddComponent<SpriteRenderer>();
        spriteRenderer.sprite = candleSprite;
        spriteRenderer.color = (closePrice > openPrice) ? Color.green : Color.red;

        LineRenderer lineRenderer = candlestick.AddComponent<LineRenderer>();
        lineRenderer.positionCount = 2;
        lineRenderer.startWidth = 0.02f;
        lineRenderer.endWidth = 0.02f;
        lineRenderer.SetPosition(0, new Vector3(num - transform.localScale.x / 2f, (highPrice - minPrice) * verticalScale / 2f, 0f));
        lineRenderer.SetPosition(1, new Vector3(num - transform.localScale.x / 2f, (lowPrice - minPrice) * verticalScale / 2f, 0f));
        lineRenderer.material = new Material(Shader.Find("Sprites/Default"));
        lineRenderer.startColor = (closePrice > openPrice) ? Color.green : Color.red;
        lineRenderer.endColor = (closePrice > openPrice) ? Color.green : Color.red;

        candlestick.transform.SetParent(transform);

    }
}
