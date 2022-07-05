##################### Grabbing MIDs data 

library(rvest)

#Specifying the url for desired website to be scraped
url <- "https://en.wikipedia.org/wiki/Maritime_identification_digits"

#Reading the HTML code from the website
webpage <- read_html(url)


#Extract ALL tables from webpage
tables <- html_table(webpage, fill=TRUE)

#Extract and assign the sole table to the dataframe 'df'
df <- tables[[1]]
# str(df) # Checking the structure of the data. I am going to have to seperate the informaiton for further use.
# head(df,10) # Seeing how the data looks.

#Extracting the MID file so I can read it into Python in order to present the transform the information into a useable product. 
new.file <- write.csv(df, "~/OneDrive/NPS/Quarter7/OA3802_Comp_III/Labs/OA3802_Lab2/data//MID.csv",row.names = FALSE)


################################ Grabbing AIS Data
s.date <-'2018_10_01'
e.date <- '2018_11_03'
new.dir <- "~/OneDrive/NPS/Quarter7/OA3802_Comp_III/Labs/OA3802_Lab2/data"

file_producer <- function(start.date = s.date, end.date = e.date, files.dir = new.dir ){
  current.dir <- getwd()
  
  # Setting directory to send files
  setwd(files.dir)
  
  start.date <-as.Date(start.date, "%Y_%m_%d")  
  end.date <-as.Date(end.date, "%Y_%m_%d")  
  Date.Range <- seq(start.date, end.date,1) 
  
  str_extract(Date.Range[i],'\\d\\d\\d\\d' ) # Year
  str_extract(Date.Range[i],'\\d\\d$' )  # Day
  str_extract(Date.Range[i],'\\b\\d\\d\\b' )  # Month
  
  # Once I fix the date range everything will work the 
  for ( i in 1:length(Date.Range)){
    # print(Date.Range[i])
    year <- str_extract(Date.Range[i],'\\d\\d\\d\\d') # Grabbing the Year
    day <- str_extract(Date.Range[i],'\\d\\d$')  # Grabbing the Day
    month <- str_extract(Date.Range[i],'\\b\\d\\d\\b')  # Grabbing the Month
    
    data <- paste('https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2018/AIS_',year,'_',month,'_',day,'.zip',sep = "") 

    # Writing data to file 
    if (i == 1){
      write(data, paste('AIS_',start.date,'.txt',sep = ""), sep ="/t") # Creating first txt file
     } else {
      write(data, file =paste('AIS_',start.date,'.txt',sep = ""), append = TRUE) # appending additional files as required
      } # Appending additional urls}}}
  }
  
  setwd(current.dir) # Returning to original directory
}  


