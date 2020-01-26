import UIKit
import GoogleMaps



class ViewController: UIViewController, CLLocationManagerDelegate {

    var locationManager = CLLocationManager()
    lazy var mapView = GMSMapView()
    var tapped : Bool = false
    var drawn : Bool = false
    private var currentLocation: CLLocation?
    //var userLocation = CLLocation()
    
    func request(type: String, Latitude: Double, Longitude: Double){
        let session = URLSession.shared
        let url = URL(string: "http://3.84.41.73:3000/")!

        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.setValue("Powered by Swift!", forHTTPHeaderField: "X-Powered-By")
        let json = [
            "name": 1,
            "tag": type,
            "coordinates": [Longitude, Latitude]
            ] as [String : Any]
        let jsonData = try! JSONSerialization.data(withJSONObject: json, options: [])
        let task = session.uploadTask(with: request, from: jsonData) { data, response, error in
            if let data = data, let dataString = String(data: data, encoding: .utf8) {
                print(dataString)
//                for (name, tag, coordinates) in data {
//                    print("\(airportCode): \(airportName)")
//                }
            }
        }

        task.resume()
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        locationManager.delegate = self
        locationManager.requestWhenInUseAuthorization()
        locationManager.desiredAccuracy = kCLLocationAccuracyBest
        locationManager.startUpdatingLocation()
    }

        func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
            currentLocation = locations.last
                        if !drawn{
            let camera = GMSCameraPosition.camera(withLatitude: currentLocation!.coordinate.latitude,longitude: currentLocation!.coordinate.longitude, zoom: 18.0)
            mapView = GMSMapView.map(withFrame: CGRect.zero, camera: camera)
            mapView.isMyLocationEnabled = true
            }
            let screenSize: CGRect = UIScreen.main.bounds
//
//            let button = UIButton(frame: CGRect(x: screenSize.width/2-75, y: 25, width: 150, height: 50))
//            button.backgroundColor = .blue
//            button.setTitle("Add Puddle", for: .normal)
//            button.addTarget(self, action: #selector(buttonAction), for: .touchUpInside)
//
//            mapView.addSubview(button)
//
//            let cbutton = UIButton(frame: CGRect(x: screenSize.width/2-75, y: 75, width: 150, height: 50))
//            cbutton.backgroundColor = .red
//            cbutton.setTitle("Add Construction", for: .normal)
//            cbutton.addTarget(self, action: #selector(constructionButtonAction), for: .touchUpInside)
//
//            mapView.addSubview(cbutton)
//
//            let pbutton = UIButton(frame: CGRect(x: screenSize.width/2-75, y: 125, width: 150, height: 50))
//            pbutton.backgroundColor = .purple
//            pbutton.setTitle("Add Crowds", for: .normal)
//            pbutton.addTarget(self, action: #selector(crowdsButtonAction), for: .touchUpInside)
//
//            mapView.addSubview(pbutton)
            
            let pimage = UIImage(named: "puddleb.png") as UIImage?
            let button = UIButton(frame: CGRect(x: screenSize.width/4-40, y: 25, width: 80, height: 80))
            //button.backgroundColor = .blue
            //button.setTitle("Add Puddle", for: .normal)
            button.setImage(pimage, for: .normal)
            button.addTarget(self, action: #selector(buttonAction), for: .touchUpInside)

            mapView.addSubview(button)
            
            let cimage = UIImage(named: "constructionb.png") as UIImage?
            let cbutton = UIButton(frame: CGRect(x: screenSize.width/2-40, y: 25, width: 80, height: 80))
            //cbutton.backgroundColor = .red
            //cbutton.setTitle("Add Construction", for: .normal)
            cbutton.setImage(cimage, for: .normal)
            cbutton.addTarget(self, action: #selector(constructionButtonAction), for: .touchUpInside)

            mapView.addSubview(cbutton)
            
            let peimage = UIImage(named: "crowdsb.png") as UIImage?
            let pbutton = UIButton(frame: CGRect(x: 3*screenSize.width/4-40, y: 25, width: 80, height: 80))
            //pbutton.backgroundColor = .purple
            //pbutton.setTitle("Add Crowds", for: .normal)
            pbutton.setImage(peimage, for: .normal)
            pbutton.addTarget(self, action: #selector(crowdsButtonAction), for: .touchUpInside)

            mapView.addSubview(pbutton)
            self.view = mapView
            drawn = true
          }

        @objc func buttonAction(sender: UIButton!) {
          print("Button tapped")
          tapped = true
            //let circleCenter = CLLocationCoordinate2D(latitude: currentLocation!.coordinate.latitude, longitude: currentLocation!.coordinate.longitude)
            //let circ = GMSCircle(position: circleCenter, radius: 10)
            //circ.map = mapView
            let position = CLLocationCoordinate2D(latitude: currentLocation!.coordinate.latitude, longitude: currentLocation!.coordinate.longitude)
            let puddle = GMSMarker(position: position)
            puddle.title = "Hello World"
            puddle.icon = UIImage(named: "puddle.png")
            puddle.map = mapView
            
            request(type: "PUDDLE", Latitude: currentLocation!.coordinate.latitude, Longitude: currentLocation!.coordinate.longitude)
    }
    
    @objc func constructionButtonAction(sender: UIButton!) {
      print("CButton tapped")
      tapped = true
        //let circleCenter = CLLocationCoordinate2D(latitude: currentLocation!.coordinate.latitude, longitude: currentLocation!.coordinate.longitude)
        //let circ = GMSCircle(position: circleCenter, radius: 10)
        //circ.map = mapView
        let position = CLLocationCoordinate2D(latitude: currentLocation!.coordinate.latitude, longitude: currentLocation!.coordinate.longitude)
        let construction = GMSMarker(position: position)
        construction.title = "Hello World"
        construction.icon = UIImage(named: "construction.png")
        construction.map = mapView
        
        request(type: "CONSTRUCTION", Latitude: currentLocation!.coordinate.latitude, Longitude: currentLocation!.coordinate.longitude)
    }
    
    @objc func crowdsButtonAction(sender: UIButton!) {
      print("CButton tapped")
      tapped = true
        //let circleCenter = CLLocationCoordinate2D(latitude: currentLocation!.coordinate.latitude, longitude: currentLocation!.coordinate.longitude)
        //let circ = GMSCircle(position: circleCenter, radius: 10)
        //circ.map = mapView
        let position = CLLocationCoordinate2D(latitude: currentLocation!.coordinate.latitude, longitude: currentLocation!.coordinate.longitude)
        let crowds = GMSMarker(position: position)
        crowds.title = "Hello World"
        crowds.icon = UIImage(named: "crowds.png")
        crowds.map = mapView
        
        request(type: "CROWDS", Latitude: currentLocation!.coordinate.latitude, Longitude: currentLocation!.coordinate.longitude)
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
}
