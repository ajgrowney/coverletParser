import json
import sys

class FunctionObj:
	def __init__(self, fcnNamespace, fcnName, fcnReport):
		self.namespace = fcnNamespace
		self.fullname = fcnName
		self.name = fcnName.split("::")[1]
		self.lines = fcnReport["Lines"]
		self.branches = fcnReport["Branches"]
		self.ignore = False
		self.covered_lines, self.missed_lines = self.lineReportCount(self.lines)
	
	def lineReportCount(self,allLins):
		lines_covered, lines_missed = 0, 0
		for line_number, times_covered in allLins.items():
			if ( times_covered == 0 ): lines_missed += 1
			else: lines_covered += 1
		
		return lines_covered, lines_missed

class CoverageHelper:
	def __init__(self,coverletpath):
		self.namespaces = []
		self.reports = []
		self.inputfilepath = coverletpath
		self.buildCoverageHelper()
	
	def buildCoverageHelper(self):
		current_reports = []
		current_namespaces = []
		with open(self.inputfilepath) as json_file:
			f = json.load(json_file)
			dlls = f.keys()
			for dll in dlls:
				for filepath, namespace in f[dll].items():
					for _name, _report in namespace.items():
						current_namespaces.append(_name)
						for _functionDefinition, _coverage in _report.items():
							fr = FunctionObj(_name,_functionDefinition,_coverage)
							current_reports.append(fr)

		current_reports.sort(key=lambda x: x.missed_lines, reverse=True)
		self.reports = current_reports
		self.namespaces = current_namespaces
	

	def menu(self):
		menuoptions = "1: View All\n" \
			"2: View Missing Coverage\n" \
			"3: Search by Function Name\n" \
			"4: Search by Namespace\n" \
			"5: Reload\n" \
			"6:Exit\n"
			
		choice = 0
		while(choice != "6"):
			print("\n------------------------")
			choice = input(menuoptions)
			print("------------------------")
			if(choice == "1"): [print(r.fullname,r.missed_lines) for r in self.reports]	
			if(choice == "2"): self.viewMissingCoverage()
			if(choice == "3"): self.searchByFunctionName(input("Function Name: "))
			if(choice == "4"): self.searchByNamespace(input("Namespace: "))	
			if(choice == "5"): self.buildCoverageHelper()
	
	def viewMissingCoverage(self):
		for r in self.reports:
			if r.missed_lines > 0: print(r.fullname, r.missed_lines) 
	
	def searchByFunctionName(self,f):
		print("-----------------------")
		for r in self.reports:
			if f in r.name: print(r.name,r.missed_lines), print("Lines:", r.lines)
	
	def searchByNamespace(self,name):
		print("-----------------------")
		namespaces_found = {}
		for r in self.reports:
			if name in r.namespace and r.missed_lines != 0:
				if r.namespace in namespaces_found: 
					namespaces_found[r.namespace].append((r.fullname,r.missed_lines,r.lines))
				else: namespaces_found[r.namespace] = [(r.fullname,r.missed_lines,r.lines)]
		
		for k,v in namespaces_found.items():
			print("\n"+k+"\n-----------------")
			for func,count,lines in v:
				print(func + " " + str(count))
				print(lines)
	



def main(filepath):
	coverageHelper = CoverageHelper(filepath)
	coverageHelper.menu()

if __name__ == '__main__':
    filepath=sys.argv[1] if len(sys.argv) > 1 else input("Enter filepath to coverage.json:")
    main(filepath)
