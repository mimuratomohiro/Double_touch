using UnityEngine;
using System.Collections;

public class ChangeColorScript : MonoBehaviour
{

    public Renderer render;
    // Use this for initialization
    void Start()
    {
        render = this.GetComponent<Renderer>();
        Debug.Log(render.material.color);

        render.material.color = Color.blue;

    }
}