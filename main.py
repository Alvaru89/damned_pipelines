from modules.module import *

def main():
    API_TOKEN = '451a038dbd144291b812346416117571af57070a'
    USERNAME = 'Alvaru89'
    BASE_URL = 'https://api.github.com/'
    KEY = 'repos/'
    OWNER = 'ta-data-mad/'
    REPO = 'dataptmad1120/'
    SEARCH = 'search/issues?q=repo:'+OWNER+REPO+'+type:pr+state:{}'
    PULLS = 'pulls?page={}&per_page=100&state={}'
    COMMITS = 'pulls/{}/commits'
    STATE = 'open'
    
    field_list1 = ['number',
               'title',
               'state',
               'created_at',
               'updated_at',
               'closed_at',
               'html_url',
               'base.repo.full_name',
               'base.ref',
               'head.repo.full_name',
               'head.ref',
               'head.repo.pushed_at']
    
    field_list2 = ['student_name',
               'number',
               'lab_name',
               'state',
               'lab_status',
               'created_at',
               'updated_at',
               'closed_at',
               'html_url',
               'base.repo.full_name',
               'base.ref',
               'head.repo.full_name',
               'head.ref',
               'head.repo.pushed_at']
    
    field_sort1 = ['lab_status',
               'lab_name',
               'student_name']
    
    field_name1 = ['Student Name',
               'PR Number',
               'Lab Name',
               'PR Status',
               'Lab Status',
               'PR Created at',
               'PR Updated at',
               'PR Closed at',
               'PR URL',
               'base repository',
               'base',
               'head repository',
               'compare',
               'Pushed at']
    
    print('getting dataframes...')
    df_pulls=get_pulls(BASE_URL, KEY, OWNER, REPO, PULLS, SEARCH, STATE, USERNAME, API_TOKEN, field_list1)
    
    print(f'dataframe imported with {df_pulls.shape}')
    print('cleaning the mess...')
    df_clean=df_status(df_pulls, BASE_URL, KEY, OWNER, REPO, COMMITS, USERNAME, API_TOKEN, field_list2)
    print('exporting clean table...')
    create_csv(df_clean, field_sort1, field_name1)    
    print('finished!')
    return
          
if __name__ == '__main__':
 
    main()