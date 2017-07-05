using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class script : MonoBehaviour {
    public GameObject name1;
    public GameObject name2;
    public GameObject name3;
    public GameObject name4;

    public Rigidbody name1_body;
    public Rigidbody name2_body;
    public Rigidbody name3_body;
    public Rigidbody name4_body;

    int t = 0;
    // Use this for initialization
    void Start () {
        name1_body = name1.GetComponent<Rigidbody>();
        name2_body = name2.GetComponent<Rigidbody>();
        name3_body = name3.GetComponent<Rigidbody>();
        name4_body = name4.GetComponent<Rigidbody>();
    }
	
	// Update is called once per frame
	void Update () {
        t += 1;
	}

    void FixedUpdate()
    {
        if (t % 20 == 0)
        {
            if ((t / 20) % 4 == 0)
            {
                Debug.Log(t);
                name1_body.freezeRotation = false;
                name1_body.AddTorque(new Vector3(1, 0, 0) * Random.Range(-150.0f, 150.0f));
                name2_body.freezeRotation = true;
                name3_body.freezeRotation = true;
                name4_body.freezeRotation = true;
            }
            if ((t / 20) % 4 == 1)
            {
                name2_body.freezeRotation = false;
                name2_body.AddTorque(new Vector3(1, 0, 0) * Random.Range(-150.0f, 150.0f));
                name1_body.freezeRotation = true;
                name3_body.freezeRotation = true;
                name4_body.freezeRotation = true;
            }
            if ((t / 20) % 4 == 2)
            {
                name3_body.freezeRotation = false;
                name3_body.AddTorque(new Vector3(1, 0, 0) * Random.Range(-150.0f, 150.0f));
                name1_body.freezeRotation = true;
                name2_body.freezeRotation = true;
                name4_body.freezeRotation = true;
            }
            if ((t / 20) % 4 == 3)
            {
                name4_body.freezeRotation = false;
                name4_body.AddTorque(new Vector3(1, 0, 0) * Random.Range(-150.0f, 150.0f));
                name1_body.freezeRotation = true;
                name2_body.freezeRotation = true;
                name3_body.freezeRotation = true;
            }
        }
    }


}
