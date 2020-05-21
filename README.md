# ISP Monitor
A tool to monitor my internet connection's data usage, payment and account status.


## TODOs
* [ ] Add support for other ISPs.
* [ ] Post a relevant message as per status and payment date.
* [x] Remove verbose by default from `isp_printer.py`
* [ ] Take care/Handle the SSL Error warnings for Jetspot. (Incomplete server certificate chain)
* [ ] Add argparse with options for
  * [ ]  dummy/demo mode (useful for my personal usage when showing someone how this works or at least the output. Mightnot be be so relevant), 
  * [x]  ~~instant mode(checkstatus for runtime-entered username, password)~~, 
  * [x]  ~~verbose mode(Print what was entirely scrapped from the ISP's website)~~
* [x] ~~Use datetime module instead of datetimeproxy.py~~
* [ ] Remove last "" at the end in `isp_parser.py`'s  `non_empty_data_list.append("") `. Will get back to this later. 
