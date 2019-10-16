import sys
import json

class FunctionReport:
	def __init__(self,namespace, n,rep):
		self.namespace = namespace
		self.fullname = n
		self.name = n.split("::")[1]
		self.lines = rep["Lines"]
		self.branches = rep["Branches"]
		self.ignore = False
		self.covered_lines, self.missed_lines = self.lineReportCount(self.lines)
	def lineReportCount(self,d):
		covered, missed = 0,0
		for k,v in d.items():
			if v==0: missed += 1
			else: covered += 1 
		return covered, missed

class ReportsContainer:
	def __init__(self):
		self.namespaces = []
		self.reports = []
	def menu(self):
		menuoptions = "1: View All\n2: View Missing Coverage\n3: Search by Function Name\n4: Search by Namespace\n5: Exit\n"
		choice = 0
		while(choice != "5"):
			print("\n------------------------")
			choice = input(menuoptions)
			print("------------------------")
			if(choice == "1"): [print(r.fullname,r.missed_lines) for r in self.reports]	
			if(choice == "2"): self.viewMissingCoverage()
			if(choice == "3"): self.searchByFunctionName(input("Function Name: "))
			if(choice == "4"): self.searchByNamespace(input("Namespace: "))	
	
	def viewMissingCoverage(self):
		for r in self.reports:
			if r.missed_lines > 0: print(r.fullname, r.missed_lines) 
	def searchByFunctionName(self,f):
		print("-----------------------")
		for r in self.reports:
			if f in r.name: print(r.name,r.missed_lines)
	def searchByNamespace(self,name):
		print("-----------------------")
		namespaces_found = {}
		for r in self.reports:
			if name in r.namespace:
				if r.namespace in namespaces_found:
					namespaces_found[r.namespace].append((r.fullname,r.missed_lines))
				else: namespaces_found[r.namespace] = [(r.fullname,r.missed_lines)]
		for k,v in namespaces_found.items():
			print("\n"+k+"\n-----------------")
			for func,count in v:
				print(func + " " + str(count))
def main():
	Reports = ReportsContainer()
	with open(sys.argv[1]) as json_file:
		f = json.load(json_file)
		dlls = f.keys()
		for dll in dlls:
			for _filepath, _namespace in f[dll].items():
				for _name, _report in _namespace.items():
					Reports.namespaces.append(_name)
					for _functionDefinition, _coverage in _report.items():
						fr = FunctionReport(_name,_functionDefinition,_coverage)
						Reports.reports.append(fr)
	
	Reports.reports.sort(key=lambda x: x.missed_lines, reverse=True)
	Reports.menu()

if __name__ == '__main__':
	main()
