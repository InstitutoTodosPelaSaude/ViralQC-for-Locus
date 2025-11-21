import os
import sys

def check_services_variables():
    '''
    Check for required environment variables.
    '''
    obligatory_env_variables = [
        'VIRALQC_API_KEY'
    ]
    missing_vars = [var for var in obligatory_env_variables if not os.getenv(var)]
    
    if missing_vars:
        return False, f'Missing environment variables:\n' + '\n'.join(missing_vars)
    return True, 'All required environment variables are set.'

def healthcheck():
    checks = {
        '.env obligatory variables Check': check_services_variables
    }
    
    all_healthy = True
    for name, check in checks.items():
        healthy, message = check()
        if not healthy:
            print(f'❌ {name} FAILED: {message}')
            all_healthy = False
        else:
            print(f'✅ {name}: {message}')
    
    sys.exit(0 if all_healthy else 1)

if __name__ == '__main__':
    healthcheck()