using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace Company.Function
{
    public class test_obtain_ip
    {
        private readonly ILogger<test_obtain_ip> _logger;

        public test_obtain_ip(ILogger<test_obtain_ip> logger)
        {
            _logger = logger;
        }

        [Function("test_obtain_ip")]
        public IActionResult Run([HttpTrigger(AuthorizationLevel.Function, "get", "post")] HttpRequest req)
        {
            _logger.LogInformation("C# HTTP trigger function processed a request.");

            // Obtener la dirección IP del cliente
            var ipAddress = req.HttpContext.Connection.RemoteIpAddress?.ToString();

            return new OkObjectResult(new { Message = "Welcome to Azure Functions!", ClientIp = ipAddress });
        }
    }
}
