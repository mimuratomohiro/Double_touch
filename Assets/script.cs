using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class script : MonoBehaviour {
    public GameObject name1;
    public GameObject name2;

    public Rigidbody name1_body;
    public Rigidbody name2_body;

    int t = 0;
    // Use this for initialization
    void Start () {
        name1_body = name1.GetComponent<Rigidbody>();
        name2_body = name2.GetComponent<Rigidbody>();
    }
	
	// Update is called once per frame
	void Update () {
        t += 1;
	}

    void FixedUpdate()
    {
        if (t % 10 == 0)
        {
            name1_body.AddTorque(new Vector3(1,0,0) * Random.Range(-150.0f, 150.0f));
            name2_body.AddTorque(new Vector3(1,0,0) * Random.Range(-150.0f, 150.0f));
        }
    }


}
