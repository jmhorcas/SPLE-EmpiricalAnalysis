library(readxl)
tools <- read_excel("K:/Mi unidad/Research/Articles/Conferences/2019 SPLC/tools.xlsx")

n_tools <- nrow(tools)

#################################################################################################


available_usable_tools <- tools[tools$AvailableUsable=='Yes',]
available_usable_tools_pct <- nrow(available_usable_tools) / n_tools
print(paste('available and usable tools: ', nrow(available_usable_tools), '(', available_usable_tools_pct*100, '%)'))

da <- tools[tools$SPLProcess=='Domain Analysis (DA)',]
ra <- tools[tools$SPLProcess=='Domain Analysis (DA)',]
di <- tools[tools$SPLProcess=='Domain Implementation (DI)',]
pd <- tools[tools$SPLProcess=='Product Derivation (PD)',]

da_ra <- tools[tools$SPLProcess=='Domain Analysis (DA), Requirements Analysis (RA)',]
di_pd <- tools[tools$SPLProcess=='Domain Implementation (DI), Product Derivation (PD)',]
da_di <- tools[tools$SPLProcess=='Domain Analysis (DA), Domain Implementation (DI)',]
ra_di <- tools[tools$SPLProcess=='Requirements Analysis (RA), Domain Implementation (DI)',]

da_ra_pd <- tools[tools$SPLProcess=='Domain Analysis (DA), Requirements Analysis (RA), Product Derivation (PD)',]
da_ra_di <- tools[tools$SPLProcess=='Domain Analysis (DA), Requirements Analysis (RA), Domain Implementation (DI)',]
all_p <- tools[tools$SPLProcess=='Domain Analysis (DA), Requirements Analysis (RA), Domain Implementation (DI), Product Derivation (PD)',]

da_count <- nrow(da) + nrow(da_ra) + nrow(da_di) + nrow(da_ra_pd) + nrow(da_ra_di) + nrow(all_p)
print(paste('Domain Analysis (DA): ', da_count, '(', (da_count/n_tools)*100, '%)'))

ra_count <- nrow(ra) + nrow(da_ra) + nrow(ra_di) + nrow(da_ra_pd) + nrow(da_ra_di) + nrow(all_p)
print(paste('Requirements Analysis (RA): ', ra_count, '(', (ra_count/n_tools)*100, '%)'))

di_count <- nrow(di) + nrow(di_pd) + nrow(da_di) + nrow(ra_di) + nrow(da_ra_di) + nrow(all_p)
print(paste('Domain Implementation (DI): ', di_count, '(', (di_count/n_tools)*100, '%)'))

pd_count <- nrow(pd) + nrow(di_pd) + nrow(da_ra_pd) + nrow(all_p)
print(paste('Product Derivation (PD): ', pd_count, '(', (pd_count/n_tools)*100, '%)'))

all_count <- nrow(all_p)
print(paste('All phases: ', all_count, '(', (all_count/n_tools)*100, '%)'))

# Simple Pie Chart
par(bg = 'transparent')
slices <- c(da_count, ra_count, di_count, pd_count, all_count)
lbls <- c("Domain\nAnalysis (DA):", "Requirements\nAnalysis (RA):", "Domain\nImplementation (DI):", "Product\nDerivation (PD):", "All phases:")
pct <- round(slices/sum(slices)*100)
lbls <- paste(lbls, pct) # add percents to labels 
lbls <- paste(lbls,"%",sep="") # ad % to labels 
#pie(slices, labels=lbls, col=rainbow(length(lbls)), main="SPL phases covered")
pie(slices, labels=lbls, col=rainbow(length(lbls)))
title("SPL phases covered", line=-1.5)

#my_colors = colorRampPalette(c("white", "black"))(5) 
#pie(slices, labels=lbls, col=c("black","white", my_colors), main="SPL phases covered by the tools")



#################################################################################################3

available_usable_tools <- tools[tools$AvailableUsable=='Yes',]
available_usable_tools_no <- tools[tools$AvailableUsable=='No',]
available_usable_tools_pct <- nrow(available_usable_tools) / n_tools
print(paste('% available and usable tools: ', available_usable_tools_pct*100, '%'))

# Simple Pie Chart
slices <- c(nrow(available_usable_tools), nrow(available_usable_tools_no))
lbls <- c("Available\nand usable:", "Not available,\ncomplex setup,\nor not working:")
pct <- round(slices/sum(slices)*100)
lbls <- paste(lbls, pct) # add percents to labels 
lbls <- paste(lbls,"%",sep="") # ad % to labels 
#pie(slices, labels=lbls, col=c("green", "red"), main="Availability and Usability")
pie(slices, labels=lbls, col=c("green", "red"))
title("Availability and Usability", line=-1.5)


#################################################################################################3
library(readxl)
tools <- read_excel("K:/Mi unidad/Research/Articles/Conferences/2019 SPLC/tools.xlsx")
#View(tools)

library(timelineS)
timelineG(df=tools, start="FirstRelease", end="LastUpdate", names="ToolName", 
          phase="AvailableUsable", group1="Space")



modeling_usa_count <- nrow(da[da$AvailableUsable=='Yes',]) + nrow(ra[ra$AvailableUsable=='Yes',]) + nrow(da_ra_pd[da_ra_pd$AvailableUsable=='Yes',]) + nrow(da_ra_di[da_ra_di$AvailableUsable=='Yes',]) + nrow(all_p[all_p$AvailableUsable=='Yes',])
modeling_nousa_count <- nrow(da[da$AvailableUsable=='No',]) + nrow(ra[ra$AvailableUsable=='No',]) + nrow(da_ra_pd[da_ra_pd$AvailableUsable=='No',]) + nrow(da_ra_di[da_ra_di$AvailableUsable=='No',]) + nrow(all_p[all_p$AvailableUsable=='No',])