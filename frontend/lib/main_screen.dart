import 'dart:convert';

import 'package:flutter/material.dart';
import 'dart:collection';
import 'dart:convert' as convert;
import 'package:http/http.dart' as http;

var result = "Result..";

class MianScreen extends StatefulWidget {
  const MianScreen({super.key});

  @override
  // ignore: library_private_types_in_public_api
  _MianScreenState createState() => _MianScreenState();
}

class _MianScreenState extends State<MianScreen> {
  int _itemCount = 0;
  var jsonResponse;
  String? _Query;
  bool? antique = false;
  bool? wikIR1k = false;
  bool? df = false;
  bool? tf = false;
  bool? idf = false;
  bool? tfidf = false;
  bool? cosinesimilarity = false;
  bool? crawler = false;
  Future<void> sendJsonToPython(query) async {
    var url = 'http://127.0.0.1:5000/api/endpoint';
    var jsonBody = jsonEncode({
      'query': '$query',
      'antique': '$antique',
      'wikIR1k': '$wikIR1k',
      'df': '$df',
      'tf': '$tf',
      'idf': '$idf',
      'tfidf': '$tfidf',
      'cosinesimilarity': '$cosinesimilarity',
      'crawler': '$crawler',
    });
    var response = await http.post(
      Uri.parse(url),
      headers: {'Content-Type': 'application/json'},
      body: jsonBody,
    );
    if (response.statusCode == 200) {
      print('JSON sent successfully');
    } else {
      print('Error sending JSON: ${response.statusCode}');
    }
    var response1 = await http.get(Uri.parse('http://127.0.0.1:5000/'));
    if (response1.statusCode == 200) {
      setState(() {
        result = response.body;
        print("********************************** : $result");
      });
      //   if (response1.statusCode == 200) {
      //     print('JSON sent successfully');
      //   } else {
      //     print('Error sending JSON: ${response.statusCode}');
      //   }
    }
  }
//   Future<void> getQuotes(query) async {
//     String url1 = "http://127.0.0.1:5000/?query=$query";
//     Uri url = Uri.parse(url1);
//     http.Response response = await http.get(url);
//     if (response.statusCode == 200) {
//       setState(() {
//         result = response.body;
//         print("********************************** : $result");
//         // jsonResponse = convert.jsonDecode(response.body);
//         // _itemCount = jsonResponse.length;
//       });
// //      jsonResponse[0]["author"]; = author name
// //      jsonResponse[0]["quote"]; = quotes text
//       // ignore: avoid_print
//       print("Number of quotes found : $_itemCount.");
//     } else {
//       // ignore: avoid_print
//       print("Request failed with status: ${response.statusCode}.");
//     }
//   }

  @override
  Widget build(BuildContext context) {
    Color getColor(Set<MaterialState> states) {
      const Set<MaterialState> interactiveStates = <MaterialState>{
        MaterialState.pressed,
        MaterialState.hovered,
        MaterialState.focused,
      };
      if (states.any(interactiveStates.contains)) {
        return Colors.blue;
      }
      return Colors.red;
    }

    var result_view;
    // bool isChecked = false;
    // int? _value = 1;

    return Container(
      decoration: BoxDecoration(
        image: DecorationImage(image: AssetImage("assets/7718877.jpg"))
      ),
      child: Center(
      child: SingleChildScrollView(
        child: Column(
          children: <Widget>[
            Container(
              height: _itemCount == 0 ? 50 : 350,
              child: _itemCount == 0
                  ? const Text(
                      "",
                      style: TextStyle(color: Color.fromARGB(255, 1, 38, 69)),
                    )
                  : ListView.builder(
                      itemBuilder: (context, index) {
                        return Container(
                          decoration: const BoxDecoration(
                              color: Colors.black12,
                              borderRadius:
                                  BorderRadius.all(Radius.circular(10))),
                          padding: const EdgeInsets.only(
                              left: 20, right: 20, top: 10),
                          margin: const EdgeInsets.symmetric(
                              vertical: 5, horizontal: 10),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: <Widget>[
                              Text(
                                jsonResponse[index]["quote"], //quote
                                style: const TextStyle(color: Colors.white),
                              ),
                              Text(
                                jsonResponse[index]["author"], //author name
                                style: const TextStyle(
                                    color: Colors.white, fontSize: 18),
                              ),
                            ],
                          ),
                        );
                      },
                      itemCount: _itemCount,
                    ),
            ),
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 20),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  TextField(
                    style:
                        const TextStyle(color: Color.fromARGB(255, 1, 38, 69)),
                    decoration: const InputDecoration(
                        hintText: "Enter the text here..",
                        contentPadding:
                            EdgeInsets.symmetric(vertical: 20, horizontal: 10),
                        enabledBorder: OutlineInputBorder(
                            borderSide: BorderSide(color: Colors.blue)),
                        focusedBorder: OutlineInputBorder(
                            borderSide: BorderSide(color: Colors.blue)),
                        border: OutlineInputBorder(
                            borderSide: BorderSide(color: Colors.blue))),
                    onChanged: (value) {
                      _Query = value;
                      // ignore: avoid_print
                      print(value);
                    },
                  ),
                  const SizedBox(
                    height: 10,
                  ),
                  ButtonTheme(
                      minWidth: 100,
                      child: ElevatedButton(
                        child: const Text(
                          "SEARCH",
                          style: TextStyle(color: Colors.white),
                        ),
                        // color: Colors.black87,
                        onPressed: () {
                          sendJsonToPython(_Query);
                          setState(() {
                            result_view = result;
                          });
                        },
                      )),
                  const SizedBox(
                    height: 10,
                  ),
                  Container(
                    height: 100,
                    width: 900,
                    decoration: BoxDecoration(
                        border: Border.all(color: Colors.blue),
                        borderRadius:
                            const BorderRadius.all(Radius.circular(10))),
                    child: SingleChildScrollView(
                        child: Padding(
                      padding: const EdgeInsets.all(10),
                      child: Text(
                        '$result',
                        style: const TextStyle(
                            color: Color.fromARGB(255, 1, 38, 69),
                            fontSize: 15),
                      ),
                    )),
                  ),
                  const SizedBox(
                    height: 10,
                  ),
                  StatefulBuilder(
                      builder: (BuildContext context, StateSetter setState) {
                    return Column(
                      children: [
                        CheckboxListTile(
                          activeColor: Colors.grey,
                          title: const Text('antique-collection'),
                          value: antique,
                          onChanged: (bool? value) {
                            setState(() {
                              antique = value;
                            });
                          },
                        ),
                        CheckboxListTile(
                          activeColor: Colors.grey,
                          title: const Text('WikIR1k'),
                          value: wikIR1k,
                          onChanged: (bool? value) {
                            setState(() {
                              wikIR1k = value;
                            });
                          },
                        ),
                        // CheckboxListTile(
                        //   title: const Text('DF'),
                        //   value: df,
                        //   onChanged: (bool? value) {
                        //     setState(() {
                        //       df = value;
                        //     });
                        //   },
                        // ),
                        // CheckboxListTile(
                        //   title: const Text('TF'),
                        //   value: tf,
                        //   onChanged: (bool? value) {
                        //     setState(() {
                        //       tf = value;
                        //     });
                        //   },
                        // ),
                        // CheckboxListTile(
                        //   title: const Text('IDF'),
                        //   value: idf,
                        //   onChanged: (bool? value) {
                        //     setState(() {
                        //       idf = value;
                        //     });
                        //   },
                        // ),
                        // CheckboxListTile(
                        //   title: const Text('TF-IDF'),
                        //   value: tfidf,
                        //   onChanged: (bool? value) {
                        //     setState(() {
                        //       tfidf = value;
                        //     });
                        //   },
                        // ),
                        CheckboxListTile(
                          activeColor: Colors.grey,
                          title: const Text('cosine_similarity'),
                          value: cosinesimilarity,
                          onChanged: (bool? value) {
                            setState(() {
                              cosinesimilarity = value;
                            });
                          },
                        ),
                        CheckboxListTile(
                          activeColor: Colors.grey,
                          title: const Text('Crawler'),
                          value: crawler,
                          onChanged: (bool? value) {
                            setState(() {
                              crawler = value;
                            });
                          },
                        )
                      ],
                    );
                  })
                ],
              ),
            ),
          ],
        ),
      ),
    ),
    );
  }
}

// RaisedButton(
//                       child: const Text(
//                         "get quotes",
//                         style: TextStyle(color: Colors.white),
//                       ),
//                       color: Colors.black87,
//                       onPressed: () {
//                         getQuotes(_Query);
//                         setState(() {
//                           _itemCount = 0;
//                         });
//                       },
//                     ),