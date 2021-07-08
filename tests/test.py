import pyshark

def print_live_notafiscal():
	capture = pyshark.LiveCapture("Ethernet", display_filter="http")
	for packet in capture:
		# if hasattr(packet, 'host'):
		# 	if "livingpharma.com.br" in packet.http.host:
		# 		print(str(packet.http.file_data))

		if hasattr(packet.http, 'host'):
			if "webservice.correios.com.br:80" in packet.http.host:
				print(str(packet.http.file_data))

		if hasattr(packet.http, 'response_for_uri'):
			if "http://webservice.correios.com.br:80/service/rastro" in packet.http.response_for_uri:
				print(str(packet.http.file_data))

		# if "DNS" in packet and not packet.dns.flags_response.int_value:
		# 	print(packet.dns.qry_name)

if __name__ == "__main__":
	print_live_notafiscal()